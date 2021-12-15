#!/usr/bin/perl -w

use strict;
use integer;

$_ = <>;
chomp;
my @c = split(',');
my @o = @c;


my $maxp = undef;
for (permutation(5 .. 9)) {
	print "perm: @{$_}\n";
	my @p = ();
	my @s = ();
	for (@{$_}) {
		push @s, [\@o, 0, [$_], []];
	}

	push @{$s[0] -> [2]}, 0; # initial 0;

	do {
		my $amp;
		for $amp (0 .. 4) {
			$s[$amp] = [run(@{$s[$amp]})];
			print "$amp: @{$s[$amp]}\n";
			push @{$s[($amp + 1) % 5] -> [2]}, @{$s[$amp] -> [3]};
			$s[$amp] -> [3] = [];
		}
	} until ($s[4] -> [1] == -1);

	my $p = ${$s[0] -> [2]}[-1];

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
	my ($o, $ip, $in, $out) = @_;
	@c = @{$o};

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
			if (!@{$in}) {
				return ([@c], $ip - 2, $in, $out);
			}
			$c[$a] = shift @{$in};
		} elsif ($cmd == 4) {
			push @{$out}, $_a;
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

	([@c], -1, $in, $out);
}

