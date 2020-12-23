#!/usr/bin/perl -w

use strict;

my @p1 = ();
my @p2 = ();
my $p2 = 0;

while (<>) {
	chomp();
	$p2 = 1 if /^Player 2:/;
	next if /^Player/;
	next unless /\d+/;

	if ($p2) {
		push @p2, $_;
	} else {
		push @p1, $_;
	}
}

while (scalar(@p1) * scalar(@p2)) {
	my $p1 = shift @p1;
	my $p2 = shift @p2;

	if ($p1 > $p2) {
		push @p1, $p1, $p2;
	} else {
		push @p2, $p2, $p1;
	}
}

if (scalar(@p2)) {
	@p1 = @p2;
}

my $out = 0;
while (@p1) {
	$out += scalar(@p1) * (shift @p1);
}

print "$out\n";


