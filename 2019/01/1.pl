#!/usr/bin/perl -w

use strict;
use integer;

my $s = 0;
my $s2 = 0;
while (<>) {
	chomp();
	$s += int($_ / 3) - 2;
	$s2 -= $_;
	do {
		$s2 += $_;
		$_ = int($_ / 3) - 2;
	} while ($_ > 0);
}

print "$s\n";
print "$s2\n";

