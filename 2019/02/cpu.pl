#!/usr/bin/perl -w

use strict;
use integer;

$_ = <>;
chomp;
my @c = split(',');
my @o = @c;


my ($i, $j);

for $i (0 .. 99) {
	for $j (0 .. 99) {
		if (run($i, $j) == 19690720) {
			print $i * 100 + $j, "\n";
		}
	}
}


sub run {
	my $ip = 0;

	@c = @o;

	($c[1], $c[2]) = @_[0, 1];

	while ($c[$ip] == 1 || $c[$ip] == 2) {
		my $op = $c[$ip++];
		my $a = $c[$ip++];
		my $b = $c[$ip++];
		my $c = $c[$ip++];

		$c[$c] = $op == 1 ? ($c[$a] + $c[$b]) : ($c[$a] * $c[$b]);
	}

	return $c[0];
}

