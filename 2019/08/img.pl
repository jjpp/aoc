#!/usr/bin/perl -w

use strict;

my @img = split '', <>;
pop @img;

my ($min0, $minp) = (151, 0);

my @out = ();

while (@img) {
	my %c = ();
	$c{0} = 0;
	$c{1} = 0;
	$c{2} = 0;
	for (0 .. (25 * 6 - 1)) {
		my $p = shift @img;
		$c{$p} ++;
		$out[$_] = $p if (!defined($out[$_]) || $out[$_] == 2);
	}
	if ($c{0} < $min0) {
		$min0 = $c{0};
		$minp = $c{1} * $c{2};
	}
}

print "$minp\n";

my @p = ('.', '#', ' ');
for (1 .. (25 * 6)) {
	print $p[$out[$_ - 1]];
	print "\n" unless $_ % 25;
}

print "\n";

