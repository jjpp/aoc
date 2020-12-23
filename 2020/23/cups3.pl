#!/usr/bin/perl -w

use strict;

my $cin = <>;
chomp $cin;
my @c = split '', $cin;

my $next = scalar(@c) + 1;
my %next = ();

my $first;
while (@c) {
	$first = pop @c;
	$next{$first} = $next;
	$next = $first;
}

for (length($cin) + 1 .. 1_000_000 - 1) {
	$next{$_} = $_ + 1;
}

$next{1000000} = substr($cin, $[, 1);

my $n = substr($cin, $[, 1);
for (1 .. 15) {
	print "$n ";
	$n = $next{$n};
}

print ".. $next{1000000}\n";

for (1 .. 10_000_000) {
	print "$_\n" unless $_ % 10000;
	$first = move($first);
}

my $i2 = $next{1};
my $i3 = $next{$i2};

print $i2 * $i3, "\n";



sub move {
	my $current = $_[0];
	my $n = scalar(keys %next);

	my $d = $current - 1;
	$d = $n if $d < 1;
	my $a = $next{$current};
	my $b = $next{$a};
	my $c = $next{$b};

	while ($d == $a || $d == $b || $d == $c) {
		$d--;
		if($d < 1) {
			$d = $n;
		}
	}

	$next{$current} = $next{$c};
	$next{$c} = $next{$d};
	$next{$d} = $a;

	$next{$current};
}


