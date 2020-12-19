#!/usr/bin/perl -w

use strict;
use integer;
use bigint;

$_ = <>;
chomp;
my @c = split(',');
my @o = @c;

my @mode = ('ind', 'dir', 'rel');

my $debug = 0;

run(0);
run(1);


sub zero {
	defined($_[0]) ? $_[0] : 0;
}

sub rd {
	my ($c, $rb, $mode, $a) = @_;
	return zero($c -> [$a]) if ($mode == 0);
	return $a if ($mode == 1);
	return zero($c -> [$rb + $a]) if ($mode == 2);
	die "invalid read mode $mode?\n";
}

sub wr {
	my ($c, $rb, $mode, $a, $v) = @_;
	return $c -> [$a] = $v if $mode == 0;
	return $c -> [$rb + $a] = $v if $mode == 2;
	die "invalid write param mode $mode";
}

sub run {
	my $ip = 0;
	my $rb = 0;
	my @out = ();

	my ($x, $y) = (0, 0);
	my ($dx, $dy) = (0, -1);
	my %p = ();
	my $idx = 1;

	$p{0, 0} = shift @_;

	my ($minx, $maxx, $miny, $maxy) = (undef, undef, undef, undef);

	@c = @o;

	while ($c[$ip] % 100 != 99) {
		my $op = $c[$ip++];
		my $cmd = $op % 100;
		my ($ai, $bi, $ci) = ((($op / 100) % 10) & 3, (($op / 1000) % 10) & 3, (($op / 10000) % 10) & 3);
		my ($a, $b, $c) = (undef, undef, undef);

		$a = $c[$ip++];
		
		$b = $c[$ip++] if $cmd =~ /[125678]/;
		$c = $c[$ip++] if $cmd =~ /[1278]/;


		my $_a = defined($a) ? rd(\@c, $rb, $ai, $a) : undef;
		my $_b = defined($b) ? rd(\@c, $rb, $bi, $b) : undef;
		my $_c = defined($c) ? rd(\@c, $rb, $ci, $c) : undef;

		if ($debug) {
			print "$op: $cmd, $mode[$ai], $mode[$bi], $mode[$ci]: $a ($_a)";
			print ", $b ($_b)" if defined($b);
			print ", $c ($_c)" if defined($c);
			print "\n";
		}

		if ($cmd == 3) {
			my $in = $p{$x, $y} // 0;
			wr(\@c, $rb, $ai, $a, $in);
		} elsif ($cmd == 4) {
			if ($idx ++ % 2) {
				$p{$x, $y} = $_a;
			} else {
				($dx, $dy) = !$_a ? ($dy, -$dx) : (-$dy, $dx);
				$x += $dx;
				$y += $dy;

				$minx = ($minx < $x) ? $minx : $x;
				$maxx = ($maxx > $x) ? $maxx : $x;
				$miny = ($miny < $y) ? $miny : $y;
				$maxy = ($maxy > $y) ? $maxy : $y;
			}
		} elsif ($cmd == 5) {
			$ip = $_b if $_a;
		} elsif ($cmd == 6) {
			$ip = $_b unless $_a;
		} elsif ($cmd == 7) {
			wr(\@c, $rb, $ci, $c, ($_a < $_b) ? 1 : 0);
		} elsif ($cmd == 8) {
			wr(\@c, $rb, $ci, $c, ($_a == $_b) ? 1 : 0);
		} elsif ($cmd == 9) {
			$rb += $_a;
		} else {
			wr(\@c, $rb, $ci, $c, $cmd == 1 ? $_a + $_b : $_a * $_b);
		}
	}

	print scalar(keys %p), "\n";

	for $y ($miny .. $maxy) {
		for $x ($minx .. $maxx) {
			print (($p{$x, $y} // 0) ? "#" : " ");
		}
		print "\n";
	}
}

