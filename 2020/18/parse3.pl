#!/usr/bin/perl -w

use strict;

my $s = 0;

while (<>) {
	chomp();

	$s += parse(lex($_));
}

print "$s\n";

sub parse {
	my @in = @_;
	my @s = ();

	while (@in) {
		$_ = shift @in;

		if (/\d/) {
			if (scalar(@s) > 0 && $s[-1] eq '+') {
				pop @s; # skip +
				$_ += pop @s;
			}
		} elsif (/\*/) {
			$_ = pop @s;
		} elsif (/\)/) {
			my $prod = 1;
			while (@s && ($_ = pop @s) ne '(') {
				$prod *= $_;
			}
			unshift @in, $prod;
			next;
		}

		push @s, $_;
	}

	my $prod = pop @s;
	while (@s) {
		$prod *= pop @s;
	}

	return $prod;
}

sub lex {
	my @out = ();
	my $d = 0;

	my @in = split('', $_[0]);
	while (@in) {
		$_ = shift @in;
		next if (/\s/);
		if (/\d/) {
			$d = $_;
			while (@in && $in[0] =~ /\d/) {
				$d = ($d * 10) + (shift @in);
			}
			push @out, $d;
		} else {
			push @out, $_;
		}
	}

	@out;
}
