#!/usr/bin/perl -w

use strict;

my @recipe = ();
my %all = ();
my %rall = ();

while (<>) {
	chomp();
	my @ingr;
	my @all = ();

	if (/^(.*)( .contains (.*).)$/) {
		@ingr = split(' ', $1);
		@all = split(', ', $3);
	} else {
		@ingr = split(' ', $_);
	}

	if (@all) {
		for (@all) {
			if (defined $all{$_}) {
				my $alh = $all{$_};
				for (keys %{$alh}) {
					my $ingr = $_;
					delete $alh -> {$ingr} unless grep { $_ eq $ingr } @ingr;
				}
			} else {
				$all{$_} = { map { $_ => 1 } @ingr };
			}
		}
	}

	print "ingr: @ingr\n";
	print " all: @all\n";
	
	push @recipe, [\@ingr, \@all];
}

my %bad = ();
for (keys %all) {
	print "pot in $_:";
	for (keys %{$all{$_}}) {
		print " $_";
		$bad{$_} = 1;
	}
	print "\n";
}

print "bad: ", join(", ", keys %bad), "\n";

my $c = 0;
for (@recipe) {
	$c += scalar(grep { !$bad{$_} } @{$_ -> [0]});
}

print "$c\n";

for (keys %all) {
	if (scalar(keys %{$all{$_}}) == 1) {
		$rall{(keys %{$all{$_}})[0]} = $_;
	}
}

my @solve = grep { scalar(keys %{$all{$_}}) > 1 } (keys %all);
while (@solve) {
	for (@solve) {
		my $alh = $all{$_};
		for (keys %{$alh}) {
			if (defined $rall{$_}) {
				delete $alh -> {$_};
			}
		}
		if (scalar(keys %{$alh}) == 1) {
			$rall{(keys %{$alh})[0]} = $_;
		}
	}
	@solve = grep { scalar(keys %{$all{$_}}) > 1 } (keys %all);
}

my @cdl = sort { $rall{$a} cmp $rall{$b} } (keys %rall);
print join(",", @cdl), "\n";


