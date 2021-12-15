#!/usr/bin/perl -w

use strict;

my %f = ();

while (<>) {
	chomp();
	flip($_);
}

my $p1 = scalar(grep { $_ == 1 } (values %f));

print "$p1\n";

sub flip {
	my @m = split('', $_[0]);
	my ($x, $y) = (0, 0);

	while (@m) {
		my $d = shift @m;
		if ($d eq 'e') {
			$x ++;
		} elsif ($d eq 'w') {
			$x --;
		} elsif ($d eq 's') {
			$y ++;
			my $d2 = shift @m;
			if ($d2 eq 'e') {
				$x ++;
			} else {
				# nop
			}
		} elsif ($d eq 'n') {
			$y --;
			my $d2 = shift @m;
			if ($d2 eq 'w') {
				$x --;
			} else {
				# nop;
			}
		}
	}

	print "x = $x, y = $y\n";

	$f{$x, $y} = 1 - ($f{$x, $y} // 0);
}
