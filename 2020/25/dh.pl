#!/usr/bin/perl -w

use strict;
use bigint;

my $N = 20201227;

my @pubs = <>;
chomp @pubs;

my $priv1 = solve($pubs[0]);
print "$priv1\n";

my $priv2 = solve($pubs[1]);
print "$priv2\n";

print ((7 ** ($priv1 * $priv2)) % $N, "\n");

sub solve {
	my $x = shift @_;

	my $z = 7;

	for (1 .. $N - 1) {
		return $_ if $z == $x;
		$z *= 7;
		$z %= $N;
	}

	die "Failed?";
}
