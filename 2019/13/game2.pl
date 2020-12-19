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


run();

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

	@c = @o;
	$c[0] = 2;

	my @out = ();
	my %screen = ();
	my ($maxx, $maxy) = (40, 23);
	my $score = 0;
	my $ball = undef;
	my $paddle = undef;
	my $ob = 420;

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
			my $nb = scalar(grep { $_ == 2 } (values %screen));
			my $bd = $ob - $nb;
			$ob = $nb;
			if ($bd > 0) {
				printscreen(\%screen, $maxx, $maxy);
				print "$screen{-1,0} $nb $bd\n";
			}
			my $in = $ball <=> $paddle;
			#print "ball: $ball, paddle: $paddle, $in\n";
			wr(\@c, $rb, $ai, $a, $in);
		} elsif ($cmd == 4) {
			push @out, $_a;

			if (@out == 3) {
				#$maxx = ($maxx > $out[0]) ? $maxx : $out[0];
				#$maxy = ($maxy > $out[1]) ? $maxy : $out[1];
				$ball = $out[0] if ($out[2] == 4);
				$paddle = $out[0] if ($out[2] == 3);
				$screen{$out[0], $out[1]} = $out[2];
				@out = ();
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

	print "final score: $screen{-1, 0}\n";
}

sub printscreen {
	my ($s, $mx, $my) = @_;
	my @f = split('', ' #+-o');

	my ($x, $y);

	for $y (0 .. $my) {
		for $x (0 .. $mx) {
			print $f[$s -> {$x, $y}];
		}
		print "\n";
	}
	print "score: $s->{-1,0}\n";
}
