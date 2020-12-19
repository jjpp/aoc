#!/usr/bin/perl -w

use strict;

my $n = <>;
chomp $n;
my @n = split(',', $n);

my %p = ();

for (0 .. $#n) {
	$pp{$n[$_]} = $p{$n[$_]} if defined($p{$n[$_]});
	$p{$n[$_]} = $_;
}

while ($#n <= 30000000) {
	my $p = undef;
	push @n, defined($p{$n[$#n]}) ? $#n - $p{$n[$#n]} : 0;
	$p{$n[$#n - 1]} = $#n - 1;
}

print "$n[2019]\n";
print "$n[29999999]\n";

exit 0;

while ($#n <= 30000000) {
	my $p = undef;
	for (0 .. $#n - 1) {
		$p = $_ if ($n[$_] == $n[$#n]);
	}
	push @n, defined($p) ? $#n - $p : 0;
}


