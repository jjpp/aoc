#!/usr/bin/perl -w

use strict;

my (@x, @y, @z);
my @vx = (0, 0, 0, 0);
my @vy = (0, 0, 0, 0);
my @vz = (0, 0, 0, 0);

my $iter = shift @ARGV;

for (0..3) {
	my $l = <>;
	$l =~ /<x=(-?\d+), y=(-?\d+), z=(-?\d+)>/ or die "line $l does not match?";
	$x[$_] = $1;
	$y[$_] = $2;
	$z[$_] = $3;
}


my ($a, $b);
for (1 .. $iter) {
	for $a (0 .. 2) {
		for $b ($a + 1 .. 3) {
			$vx[$a] -= $x[$a] <=> $x[$b];
			$vx[$b] += $x[$a] <=> $x[$b];
			$vy[$a] -= $y[$a] <=> $y[$b];
			$vy[$b] += $y[$a] <=> $y[$b];
			$vz[$a] -= $z[$a] <=> $z[$b];
			$vz[$b] += $z[$a] <=> $z[$b];
		}
	}

	for $a (0 .. 3) {
		$x[$a] += $vx[$a];
		$y[$a] += $vy[$a];
		$z[$a] += $vz[$a];
	}

	for $a (0 .. 3) {
		print "<$x[$a], $y[$a], $z[$a]>, <$vx[$a], $vy[$a], $vz[$a]>\n";
	}
	print "\n";
}

my $e = 0;

for $a (0 .. 3) {
	$e += (abs($x[$a]) + abs($y[$a]) + abs($z[$a])) * (abs($vx[$a]) + abs($vy[$a]) + abs($vz[$a]));
}

print "$e\n";

