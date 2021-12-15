#!/usr/bin/perl -w

use strict;
use integer;

my $N = 20201227;

my @pubs = <>;
chomp @pubs;

my $priv1 = solve($pubs[0]);
print "$priv1\n";

my $o = $pubs[1];
for (1 .. $priv1 - 1) {
	$o *= $pubs[1];
	$o %= $N;
}

print "$o\n";

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
