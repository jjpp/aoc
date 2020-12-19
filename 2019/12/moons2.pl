#!/usr/bin/perl -w

use strict;
use v5.10.1;

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

my @ox = (@x);
my @oy = (@y);
my @oz = (@z);

my @s = (undef, undef, undef);


my ($a, $b);
my $step = 0;
my @nulls = (0, 0, 0, 0);
while (!defined($s[0]) || !defined($s[1]) || !defined($s[2])) {
	$step ++;
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

	if (!defined($s[0]) && (@vx ~~ @nulls) && (@x ~~ @ox)) {
		$s[0] = $step;
		print "loop for x at $step\n";
	}

	if (!defined($s[1]) && (@vy ~~ @nulls) && (@y ~~ @oy)) {
		$s[1] = $step;
		print "loop for y at $step\n";
	}

	if (!defined($s[2]) && (@vz ~~ @nulls) && (@z ~~ @oz)) {
		$s[2] = $step;
		print "loop for z at $step\n";
	}
}

print "@s\n";

my $loop = $s[0] * $s[1] / gcd($s[0], $s[1]);
$loop = $loop * $s[2] / gcd($loop, $s[2]);

print "$loop\n";

sub gcd {
	@_ = ($_[1], $_[0]) if ($_[0] < $_[1]);
	while ($_[1] != 0) {
		push @_, $_[0] % $_[1];
		shift @_;
	}
	$_[0];
}
