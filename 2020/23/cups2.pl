#!/usr/bin/perl -w

use strict;

my $cin = <>;
chomp $cin;
my @c = split '', $cin;

my $next = 0;

for (@c) {
	$next = ($next < $_ + 1) ? $_ + 1 : $next;
}

while (scalar(@c) < 1000000) {
	push @c, $next;
	$next ++;
}

print "c generated\n";

my %prev = ();
my @s = sort @c;
my $prev = $s[$#s];
for (@s) {
	$prev{$_} = $prev;
	$prev = $_;
}

my $c = \@c;
my $curr = 0;

for (1 .. 10_000_000) {
	print "$_\n" if ($_ % 10 == 0);
	($c, $curr) = move($c, $curr);
}

@c = @{$c};

print "final: @c\n";

my $i1 = 0;

while ($c[$i1] ne 1) { 
	$i1++;
}

print ($c[($i1 + 1) % scalar(@c)] * $c[($i1 + 2) % scalar(@c)], "\n");




sub move {
	my ($c, $curr) = @_;

	# print "$c->[0] $c->[1] $c->[2] $c->[3] $c->[4] ..\n";

	my $current = $c -> [$curr];
	my $n = scalar @{$c};

	my @pu = splice(@{$c}, $curr + 1, 3);

	my $d = $current - 1;
	while ($d == $pu[0] || $d == $pu[1] || $d == $pu[2]) {
		$d--;
		$d = $n if $d < 1;
	}

	#print "d = $d\n";

	
	my $pos = 0;
	while ($c -> [$pos] ne $d) { $pos ++ }
	splice @{$c}, $pos + 1, 0, @pu;

	$curr = ($curr + 1) % $n;

	($c, $curr);
}


