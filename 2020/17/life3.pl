#!/usr/bin/perl -w

use integer;
use strict;

my %w = ();
my $mx = 0;

while (<>) {
	chomp();

	$mx = length($_);

	my $c = 0;
	for (split('')) {
		$w{$c++, $., 0} = $_;
	}
}

my $c = 0;
for (1 .. 6) {
	$c = step($_);
}

print "$c\n";

sub count {
	my ($x, $y, $z) = @_;
	my ($dx, $dy, $dz);

	my $c = 0;

	for $dx (-1 .. 1) {
		for $dy (-1 .. 1) {
			for $dz (-1 .. 1) {
				next if ($dx == 0 && $dy == 0 && $dz == 0);
				$c ++ if defined($w{($x + $dx), ($y + $dy), ($z + $dz)}) && $w{($x + $dx), ($y + $dy), ($z + $dz)} eq '#';
			}
		}
	}

	return $c;
}

sub step {
	my $s = shift @_;
	my ($x, $y, $z);

	my %nw = ();
	my $tc = 0;

	print "\nstep $s:\n";

	for $z ((0 - $s) .. (0 + $s)) {
		print "z=$z:\n";
		for $x ((0 - $s) .. ($mx + $s)) {
			for $y ((0 - $s) .. ($mx + $s)) {
				my $c = count($x, $y, $z);

				if (defined($w{$x, $y, $z}) && $w{$x, $y, $z} eq '#') {
					$nw{$x, $y, $z} = ($c == 2 || $c == 3) ? '#' : '.';
				} elsif (!defined($w{$x, $y, $z}) || $w{$x, $y, $z} ne '#') {
					$nw{$x, $y, $z} = ($c == 3) ? '#' : '.';
				}

				$tc ++ if $nw{$x, $y, $z} eq '#';
				print $nw{$x, $y, $z};
			}
			print "\n";
		}
	}

	%w = %nw;
	return $tc;
}
