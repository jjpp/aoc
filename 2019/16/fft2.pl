#!/usr/bin/perl -w

use strict;
use integer;

my $l = <>;
chomp($l);

my @in = split('', $l);
@in = (@in) x 5000;

my @mul = (0, -1, 0, 1);
my $offset = substr($l, $[, 7) + 0;

for (1 .. 100) {
	my @out = ();

	my $row;
	my $p = 0;
	for $row (0 .. $#in) {
		$out[$#in - $row] = ($p + $in[$#in - $row]) % 10;
		$p = $out[$#in - $row];
	}
	@in = @out;
	print "It $_ complete\n";
}

print "at $offset\n";
$offset -= scalar(@in); 

print @in[$offset .. $offset + 7], "\n";

