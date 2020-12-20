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

my @dx = (undef, 0, 0, -1, 1);
my @dy = (undef, -1, 1, 0, 0);

my ($map, $ox, $oy) = run(1);

my %dist = ();
$dist{$ox, $oy} = 0;
my $step = 0;
while (1) {
	my @s = grep { $dist{$_} == $step } (keys %dist);
	for (@s) {
		my ($x, $y) = split($;);
		my $d;
		for $d (1 .. 4) {
			my ($x_, $y_) = ($x + $dx[$d], $y + $dy[$d]);
			if (!defined($dist{$x_, $y_}) && $map -> {$x_, $y_} ne '#') {
				$dist{$x_, $y_} = $step + 1;
			}
		}
	}
	$step++;
	last unless @s;
}

print "p1: $dist{0,0}\n";
print "p2: ", $step - 2, "\n";

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

	my ($x, $y) = (0, 0);
	my @mr = (undef, 'A', 'V', '<', '>');
	my %map = ();
	my %seenx = ();
	my %seeny = ();
	my $ld = undef;
	my $lw = undef;
	my $step = 0;
	my ($ox, $oy);

	$map{0, 0} = '.';

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
			print "No input?\n" unless @_;
			wr(\@c, $rb, $ai, $a, $ld = shift @_);
		} elsif ($cmd == 4) {
			# print "cmd: $ld, response: $_a\n";
			if ($_a == 0) {
				$map{$x + $dx[$ld], $y + $dy[$ld]} = '#';
				$seenx{$x + $dx[$ld]} = 1;
				$seeny{$y + $dy[$ld]} = 1;
				$lw = $ld;
			} elsif ($_a == 1) {
				$x += $dx[$ld];
				$y += $dy[$ld];
				$map{$x, $y} = '.';
			} elsif ($_a == 2) {
				$x += $dx[$ld];
				$y += $dy[$ld];
				$map{$x, $y} = 'o';
				($ox, $oy) = ($x, $y);
			}

			$seenx{$x} = 1;
			$seeny{$y} = 1;
			
			if ($lw == 1) {
				if (($map{$x + $dx[$lw], $y + $dy[$lw]} // '?') eq '#') {
					$ld = 4;
				} else {
					$ld = $lw;
					$lw = 3;
				}
			} elsif ($lw == 2) {
				if (($map{$x + $dx[$lw], $y + $dy[$lw]} // '?') eq '#') {
					$ld = 3;
				} else {
					$ld = $lw;
					$lw = 4;
				}
			} elsif ($lw == 3) {
				if (($map{$x + $dx[$lw], $y + $dy[$lw]} // '?') eq '#') {
					$ld = 1;
				} else {
					$ld = $lw;
					$lw = 2;
				}
			} elsif ($lw == 4) {
				if (($map{$x + $dx[$lw], $y + $dy[$lw]} // '?') eq '#') {
					$ld = 2;
				} else {
					$ld = $lw;
					$lw = 1;
				}
			}

			push @_, $ld;

			my @v = sort { our($a, $b); $a <=> $b } (keys %seenx);
			my ($minx, $maxx) = @v[0, $#v];
			@v = sort { our($a, $b); $a <=> $b } (keys %seeny);
			my ($miny, $maxy) = @v[0, $#v];

			# print "($x, $y), ($minx, $miny), ($maxx, $maxy)\n";

			if (!($step ++ % 100)) {
			my ($x_, $y_);
			for $y_ ($miny .. $maxy) {
				for $x_ ($minx .. $maxx) {
					if ($x_ == $x && $y_ == $y) {
						print $mr[$ld];
						next;
					}
					print $map{$x_, $y_} // ' ';
				}
				print "\n";
			}
			print "\n";
			}
			# return if $map{$x, $y} eq 'o';
			if ($_a == 1 && $x == 0 && $y == 0) {
				my ($x_, $y_);
				for $y_ ($miny .. $maxy) {
					for $x_ ($minx .. $maxx) {
						if ($x_ == $x && $y_ == $y) {
							print $mr[$ld];
							next;
						}
						print $map{$x_, $y_} // ' ';
					}
					print "\n";
				}
				print "\n";
				return (\%map, $ox, $oy);
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
}

