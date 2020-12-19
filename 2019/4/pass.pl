#!/usr/bin/perl

use strict;
use integer;

my $i = <>;
chomp $i;
my ($min, $max) = (split '-', $i);

my $c = 0;

for ($min .. $max) {
	$c ++ if matches($_);
}

print "$c\n";

sub matches {
	my $p = undef;
	my $ch = 0;
	my $c2 = 0;
	my $l = 1;
	for (split '', $_[0]) {
		if (defined $p) {
			return 0 if ($_ < $p);
			if ($_ == $p) {
				$ch++;
				$l ++;
			} else {
				$c2 ++ if ($l == 2);
				$l = 1;
			}
		}
		$p = $_;
	}

	$ch && ($c2 || $l == 2);
}
