#!/usr/bin/perl -w

use strict;
use re 'strict';

my %r = ();
my $rm = 0;
my $count = 0;
my $regex = undef;

while (<>) {
	chomp();
	if (/^$/) {
		$rm = 1;
		buildrexes();
		$regex = "^" . $r{0}->[0] . '$';
		print "regex for 0: $regex\n";
		next;
	}

	if (!$rm) {
		my @d = split(' ');
		my $k = substr($d[0], 0, length($d[0]) - 1);
		if ($#d == 1) {
			$r{$k} = [substr($d[1], 1, length($d[1]) - 2)];
		} else {
			$r{$k} = [undef, []];
			shift @d;
			while (@d) {
				my $v = shift @d;
				if ($v eq '|') {
					push @{$r{$k}}, [];
				} else {
					push @{$r{$k} -> [-1]}, $v;
				}
			}
		}
	} else {
		$count ++ if /$regex/n;
		#		print "$_: ", /$regex/ ? "yes" : "no", "\n";
	}
}

print "$count\n";

sub buildrexes {
	my $c;
	do {
		$c = 0;
		key:
		for (keys %r) {
			next if defined $r{$_} -> [0];
			my @sm = map { submask(@{$_}) } @{$r{$_}}[1 .. $#{$r{$_}}];
			for (@sm) {
				next key unless defined($_);
			}
			if (@sm == 1) {
				$r{$_} -> [0] = $sm[0];
			} else {
				$r{$_} -> [0] = "(" . join('|', @sm) . ")";
			}
			$c ++;
		}
	} while ($c > 0);

}

sub submask {
	for (@_) {
		return undef unless defined $r{$_} -> [0];
	}
	join('', map { $r{$_} -> [0] } @_);
}
