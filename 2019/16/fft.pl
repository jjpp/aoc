#!/usr/bin/perl -w

use strict;
use integer;

my $l = <>;
chomp($l);

my @in = split('', $l);
@in = (@in) x 10000;

my @mul = (0, -1, 0, 1);
my $offset = substr($l, $[, 7) + 0;

for (1 .. 100) {
	my @out = ();

	my $row;
	for $row (1 .. scalar(@in)) {
		my $s = 0;
		for (0 .. $#in) {
			my $mul = $mul[($_ + 1) % ($row * 4) / $row];
			printf "%3d", $mul;
			next unless $mul;
			$s += $in[$_] * $mul;
		}
		print "\n";
		push @out, abs($s % 10);
	}
	print "iteration $_ complete\n";
	@in = @out;
}

print "at $offset\n";

print @in[$offset .. $offset + 7], "\n";

