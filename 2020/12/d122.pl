#!/usr/bin/perl

$d = 'E';
$n = 1;
$e = 10;
$dn = 0;
$de = 1;
$ln = 0;
$le = 0;

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
		$ln += ($n * $p);
		$le += ($e * $p);
	} elsif ($c eq 'R') {
		if ($p == 90) {
			($n, $e) = (-$e, $n);
		} elsif ($p == 180) {
			($n, $e) = (-$n, -$e);
		} elsif ($p == 270) {
			($n, $e) = ($e, -$n);
		}
	} elsif ($c eq 'L') {
		if ($p == 90) {
			($n, $e) = ($e, -$n);
		} elsif ($p == 180) {
			($n, $e) = (-$n, -$e);
		} elsif ($p == 270) {
			($n, $e) = (-$e, $n);
		}
	}

	print "$c, $p, ($e, $n), ($le, $ln)\n";

}

print abs($ln) + abs($le), "\n";

