#!/usr/bin/perl -w

use strict;

my @a = ();

while (<>) {
	chomp();
	my $y = $. - 1;
	my $x;
	for $x (0 .. length($_) - 1) {
		push @a, [$x, $y] if substr($_, $x, 1) eq '#';
	}
}

my @c = ();
my $maxc = 0;
my $maxa = undef;
my @maxall = ();
my @all = ();

print scalar(@a), " asteroids\n";

my $pi = atan2(0, -1);

my ($a, $b);
for $a (0 .. $#a) {
	my %dirs = ();
	my @all = ();
	for $b (0 .. $#a) {
		next if $a == $b;

		my $dx = $a[$b] -> [0] - $a[$a] -> [0];
		my $dy = $a[$b] -> [1] - $a[$a] -> [1];

		my $gcd = gcd(abs($dx), abs($dy));

		my $d = $dx * $dx + $dy * $dy;

		$dx /= $gcd;
		$dy /= $gcd;

		my $at = atan2($dx, -$dy);
		$at += (2 * $pi) if $at < 0;

		push @all, [$at, $dx, $dy, $d, $b];
	
		$dirs{$dx, $dy} ++;
	}

	$c[$a] = scalar(keys %dirs);

	if ($c[$a] > $maxc) {
		$maxc = $c[$a];
		$maxa = $a;
		@maxall = (@all);
	}
}

print "$maxc\n";
print "station at $maxa\n";

@all = @maxall;

@all = sort { our($a, $b); ($a -> [0] <=> $b -> [0]) || ($a -> [3] <=> $b -> [3]); } @all;
for (1 .. $#all) {
	if ($all[$_ - 1] -> [1] == $all[$_] -> [1] && $all[$_ - 1] -> [2] == $all[$_] -> [2]) {
		$all[$_] -> [0] = $all[$_ - 1] -> [0] + (2 * $pi);
	}
}

@all = sort { our ($a, $b); $a -> [0] <=> $b -> [0] } @all;


for (0 .. $#all) {
	my @w = @{$a[$all[$_] -> [4]]};
	print "$_: @{$all[$_]}; @w\n";
}




sub gcd {
	if ($_[0] < $_[1]) {
		@_ = @_[1, 0];
	}

	while ($_[1] != 0) {
		push @_, ($_[0] % $_[1]);
		shift @_;
	}

	return $_[0]; 
}
