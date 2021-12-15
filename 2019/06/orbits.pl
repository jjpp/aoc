#!/usr/bin/perl -w

use strict;
use integer;

my @p = ();
my $c = 0;
my %c = ('COM' => 0);
my @s = ('COM');
my %path = ('COM' => ['COM']);

while (<>) {
	chomp();
	my ($a, $b) = split('\)');

	push @p, [$a, $b];
}

while (@s) {
	my $x = pop @s;

	for (@p) {
		next unless $_ -> [0] eq $x;

		if (defined $c{$_ -> [1]}) {
			print "nontree?\n";
		}

		$c{$_ -> [1]} = $c{$_ -> [0]} + 1;
		$c += $c{$_ -> [1]}; 
		$path{$_ -> [1]} = [@{$path{$_ -> [0]}}, $_ -> [1]];
		push @s, $_ -> [1];
	}
}

print "$c\n";

print "@{$path{'YOU'}}\n";
print "@{$path{'SAN'}}\n";

while (scalar(@{$path{'YOU'}}) && scalar(@{$path{'SAN'}}) && $path{'YOU'} -> [0] eq $path{'SAN'} -> [0]) {
	shift @{$path{'YOU'}};
	shift @{$path{'SAN'}};
}

print "@{$path{'YOU'}}\n";
print "@{$path{'SAN'}}\n";

print scalar(@{$path{'YOU'}}) + scalar(@{$path{'SAN'}}) - 2, "\n";

