#!/usr/bin/perl -w

use strict;
use integer;
use bigint;

my %f = ();
my %bf = ();

while (<>) {
	chomp();
	
	my ($raw, $res) = split(' => ', $_);

	my ($rc, $rm) = split(' ', $res);

	$f{$rm} = [ $rc, [] ];
	push @{$f{$rm} -> [1]}, map { [ split(' ') ] } (split ', ', $raw);

	for (map { $_ -> [1] } @{$f{$rm} -> [1]}) {
		$bf{$rm} //= {};
		$bf{$_} //= {};
		$bf{$rm} -> {$_} = 1;
	}
}

my $c;
do {
	$c = 0;
	my ($x, $y, $z);
	for $x (keys %bf) {
		for $y (keys %bf) {
			for $z (keys %bf) {
				if ($bf{$x} -> {$y} && $bf{$y} -> {$z} && !defined($bf{$x} -> {$z})) {
					$bf{$x} -> {$z} = 1;
					$c++;
				}
			}
		}
	}
} until $c == 0;


for (keys %bf) {
	my @a = keys %{$bf{$_}};
	print "before: $_ are @a\n";
}

my @s = sort { scalar(keys %{$bf{$b}}) <=> scalar(keys %{$bf{$a}}) } (keys %bf);
print "full order: @s\n";

print "part1: ", calc(1), "\n";

my $TRILLION = 1_000_000_000_000;

my ($minf, $maxf) = (1, $TRILLION);

while ($minf < $maxf - 1) {
	my $a = $minf + ($maxf - $minf) / 2;
	my $ore = calc($a);
	print "attempted $a, needed $ore\n";
	if ($ore > $TRILLION) {
		$maxf = $a;
	} else {
		$minf = $a;
	}
}

print "part2: $minf ($maxf)\n";

sub calc {

	my %need = ('FUEL' => shift @_);

	while (scalar(keys %need) > 1 || !defined($need{'ORE'})) {
		my @s = sort { scalar(keys %{$bf{$b}}) <=> scalar(keys %{$bf{$a}}) } (keys %need);
		#print "order: @s\n";
		my $m = shift @s;
		my $n1 = $f{$m} -> [0];
		my $n = ($need{$m} + $n1 - 1) / $n1;

		#print "getting $need{$m} of $m in steps of $n1, $n sets; $unused{$m} will be left over\n";


		delete ($need{$m});
		for (@{$f{$m} -> [1]}) {
			#print " add ", $_ -> [0] * $n, " of $_->[1], ";
			$need{$_ -> [1]} += $_ -> [0] * $n;
			#print " new total $need{$_->[1]}\n";
		}
	}

	$need{'ORE'};
}


