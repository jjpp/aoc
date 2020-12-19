#!/usr/bin/perl

$d = 'E';
$n = 0;
$e = 0;
$dn = 0;
$de = 1;

$d = 0;
@dn = (0, -1, 0, 1);
@de = (1, 0, -1, 0);

while (<>) {
	chomp();
	/^([NSEWFLR])(\d+)$/;
	$c = $1;
	$p = $2;

	if ($c eq 'N') {
		$n += $p;
	} elsif ($c eq 'S') {
		$n -= $p;
	} elsif ($c eq 'E') {
		$e += $p;
	} elsif ($c eq 'W') {
		$e -= $p;
	} elsif ($c eq 'F') {
		$n += ($dn * $p);
		$e += ($de * $p);
	} elsif ($c eq 'R') {
		$p = $p / 90;
		$d = ($d + $p) % 4;
		$dn = $dn[$d];
		$de = $de[$d];
	} elsif ($c eq 'L') {
		$p = $p / 90;
		$d = (4 + $d - $p) % 4;
		$dn = $dn[$d];
		$de = $de[$d];
	}

	print "$c, $p, $de, $dn, $e, $n\n";

}

print abs($n) + abs($e), "\n";

