#!/usr/bin/perl -w

use strict;
use integer;
use bigint;

my @ranges = ();

my %f = ();

while (<>) {
	chomp;
	last unless /^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$/;
	
	$f{$1} = [[$2, $3], [$4, $5]];
	push @ranges, [$2, $3], [$4, $5];
} 


<>;
$_ = <>;
chomp;
my @mt = split(',', $_);
<>;
<>;

my $er = 0;

my @valid = ([@mt]);

while (<>) {
	chomp();

	num:
	my $n;
	my $valid = 1;
	for $n (split(',')) {
		my $r;
		if (!grep { $_ -> [0] <= $n && $_ -> [1] >= $n } @ranges) {
			$er += $n;
			$valid = 0;
		}
	}

	if ($valid) {
		push @valid, [split(',')];
	}
}

print "$er\n";

my %fp = ();

my $f;
my %pp = ();
for $f (keys %f) {
	my $p;
	for $p (0 .. $#mt) {
		if (scalar(grep { ($f{$f} -> [0] -> [0] <= $_ -> [$p] && $f{$f} -> [0] -> [1] >= $_ -> [$p]) 
				|| ($f{$f} -> [1] -> [0] <= $_ -> [$p] && $f{$f} -> [1] -> [1] >= $_ -> [$p]) } @valid) == scalar(@valid)) {
			if (!defined $pp{$f}) { $pp{$f} = [] };
			push @{$pp{$f}}, $p;
		}
	}
}

for (sort (keys %f)) {
	print "$_: @{$pp{$_}}\n";
}

my @p = (0 .. $#mt);

p:
while (@p) {
	my $p = shift @p;
	print "checking $p:\n";
	for (keys %pp) {
		print "checking for $_: @{$pp{$_}}\n";
		if (scalar(@{$pp{$_}}) == 1 && $pp{$_} -> [0] == $p) {
			print "pos $p must be $_\n";
			$fp{$_} = $p;
			for (keys %pp) {
				@{$pp{$_}} = grep { $_ != $p } @{$pp{$_}};
			}
			@p = grep { $_ != $p } @p;
			next p;
		}
	}

	my $c = 0;
	my $f = undef;
	for (keys %pp) {
		if (grep { $p == $_ } @{$pp{$_}}) {
			$f = $_;
			$c++;
		}
	}

	if ($c == 1) {
		$fp{$f} = $p;
		for (keys %pp) {
			@{$pp{$_}} = grep { $_ != $p } @{$pp{$_}};
		}
		@p = grep { $_ != $p } @p;
		next p;
	}

	push @p, $p;
}


my $prod = 1;
for (sort (keys %f)) {
	print "$_: $fp{$_} $mt[$fp{$_}]\n";
	if ($_ =~ /^departure /) {
		$prod *= $mt[$fp{$_}];
	}
}

print "$prod\n";











