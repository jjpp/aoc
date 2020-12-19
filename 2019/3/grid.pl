#!/usr/bin/perl -w

use strict;

my %g = ();
my %s = ();
my $md = undef;
my $ms = undef;

while (<>) {
	chomp();
	fill($_, $.);
}

print $md, "\n";
print $ms, "\n";

sub f0 {
	my $id = shift;
	my $c = shift;
	my $x = shift;
	my $y = shift;
	my $steps = shift;
	my $dx = shift;
	my $dy = shift;

	for (1 .. $c) {
		$x += $dx;
		$y += $dy;
		$steps ++;
		if (defined($g{$x, $y}) && ($g{$x, $y} ne $id)) {
			if (!defined($md) || $md > (abs($x) + abs($y))) {
				$md = abs($x) + abs($y);
			}
			if (!defined($ms) || $ms > ($steps + $s{$x, $y})) {
				$ms = $steps + $s{$x, $y}; 
			}
		}
		$g{$x, $y} = $id;
		$s{$x, $y} = $steps;
	}

	($x, $y, $steps);
}

sub fill {
	my $x = 0;
	my $y = 0;
	my $s = 0;
	my @c = split(',', shift @_);
	my $id = shift @_;

	for (@c) {
		/^([UDLR])(\d+)$/;
		if ($1 eq 'U') {
			($x, $y, $s) = f0($id, $2, $x, $y, $s, 0, +1);
		} elsif ($1 eq 'D') {
			($x, $y, $s) = f0($id, $2, $x, $y, $s, 0, -1);
		} elsif ($1 eq 'L') {
			($x, $y, $s) = f0($id, $2, $x, $y, $s, -1, 0);
		} elsif ($1 eq 'R') {
			($x, $y, $s) = f0($id, $2, $x, $y, $s, +1, 0);
		} 
	}
}

