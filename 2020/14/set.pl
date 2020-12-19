#!/usr/bin/perl

use bignum;
use integer;

$and = 0;
$or = 0;

@mem = ();

while (<>) {
	chomp();
	if (/^mask = (.*)$/) {
		$mask = $1;
		$am = $mask;
		$am =~ s/[01]/0/g;
		$am =~ s/X/1/g;
		$om = $mask;
		$om =~ s/X/0/g;

		print "mask:\n$am\n$om\n";

		$and = oct('0b' . $am);
		$or = oct('0b' . $om);
	} elsif (/^mem\[(\d+)] = (\d+)$/) {
		$offset = $1;
		$val = $2;
		$mem[$offset] = ($val & $and) | $or;
		print "at $offset, param $val, set $mem[$offset]\n";
	}
}

my $s = 0;
for (@mem) {
	$s += $_;
}

print "$s\n";

