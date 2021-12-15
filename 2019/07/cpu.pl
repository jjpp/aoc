#!/usr/bin/perl -w

use strict;
use integer;

$_ = <>;
chomp;
my @c = split(',');
my @o = @c;


my $maxp = undef;
for (permutation(0 .. 4)) {
	print "perm: @{$_}\n";
	my $p = 0;
	for (@{$_}) {
		$p = run($_, $p);
	}
	if (!defined($maxp) || $maxp < $p) {
		$maxp = $p;
	}
}

print "$maxp\n";

sub permutation {
	return [@_] if (scalar(@_) < 2);

	my @out = ();
	my $e;
	for $e (@_) {
		for (permutation(grep { $_ ne $e } @_)) {
			push @out, [$e, @{$_}];
		}
	}

	return @out;
}


sub run {
	my $ip = 0;

	@c = @o;

	while ($c[$ip] % 100 != 99) {
		my $op = $c[$ip++];
		my $cmd = $op % 100;
		my ($ai, $bi, $ci) = (($op / 100) & 1, ($op / 1000) & 1, ($op / 10000) & 1);
		my ($a, $b, $c) = (undef, undef, undef);

		$a = $c[$ip++];
		
		if ($cmd < 3 || $cmd > 4) {
			$b = $c[$ip++];
			$c = $c[$ip++] if ($cmd != 5 && $cmd != 6);
		}

		my $_a = defined($a) ? ($ai ? $a : $c[$a]) : undef;
		my $_b = defined($b) ? ($bi ? $b : $c[$b]) : undef;
		my $_c = defined($c) ? ($ci ? $c : $c[$c]) : undef;

		if ($cmd == 3) {
			$c[$a] = shift @_;
		} elsif ($cmd == 4) {
			print "out: $_a\n";
			return $_a;
		} elsif ($cmd == 5) {
			$ip = $_b if $_a;
		} elsif ($cmd == 6) {
			$ip = $_b unless $_a;
		} elsif ($cmd == 7) {
			$c[$c] = ($_a < $_b) ? 1 : 0;
		} elsif ($cmd == 8) {
			$c[$c] = ($_a == $_b) ? 1 : 0;
		} else {
			$c[$c] = $cmd == 1 ? $_a + $_b : $_a * $_b;
		}
	}
}

