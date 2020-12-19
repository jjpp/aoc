#!/usr/bin/perl

use integer;
use bignum;

<>;
$b = <>;
chomp($b);
@b = split(',', $b);

$a1 = 0;
$n1 = $b[0];

for $a (1 .. $#b) {
	next if $b[$a] eq 'x';
	$N = $n1 * $b[$a];

	$a2 = $b[$a] - $a;
	while ($a2 < 0) {
		$a2 += $b[$a];
	}

	($m1, $m2) = extgcd($n1, $b[$a]);
	if ($n1 < $b[$a]) {
		($m1, $m2) = ($m2, $m1);
	}

	print "$a: $a1, $b[$a], $m2; $a2, $n1, $m1; $N\n";
	print ((((($a1 * $b[$a]) % $N) * $m2) % $N), "\n");
	print ((((($a2 * $n1) % $N) * $m1) % $N), "\n");

	$x = ((((($a1 * $b[$a]) % $N) * $m2) % $N) + (((($a2 * $n1) % $N) * $m1) % $N)) % $N;

	$a1 = $x;
	$n1 = $N;
	print "$a1\n";
}

print "$a1\n";

sub extgcd {
	my ($a, $b) = @_;
	if ($a < $b) {
		($a, $b) = ($b, $a);
	}

	($old_r, $r) = ($a, $b);
	($old_s, $s) = (1, 0);
	($old_t, $t) = (0, 1);

	while ($r != 0) {
		$q = int($old_r / $r);
		($old_r, $r) = ($r, $old_r - ($q * $r));
		($old_s, $s) = ($s, $old_s - ($q * $s));
		($old_t, $t) = ($t, $old_t - ($q * $t));
	}

	return ($old_s, $old_t);
}
