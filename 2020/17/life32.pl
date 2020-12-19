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
		$w{$c++, $., 0, 0} = $_;
	}
}

my $c = 0;
for (1 .. 6) {
	$c = step($_);
}

print "$c\n";

sub count {
	my ($x, $y, $z, $w) = @_;
	my ($dx, $dy, $dz, $dw);

	my $c = 0;

	for $dx (-1 .. 1) {
		for $dy (-1 .. 1) {
			for $dz (-1 .. 1) {
				for $dw (-1 .. 1) {
					next if ($dx == 0 && $dy == 0 && $dz == 0 && $dw == 0);
					$c ++ if defined($w{($x + $dx), ($y + $dy), ($z + $dz), $w + $dw}) && $w{($x + $dx), ($y + $dy), ($z + $dz), $w + $dw} eq '#';
				}
			}
		}
	}

	return $c;
}

sub step {
	my $s = shift @_;
	my ($x, $y, $z, $w);

	my %nw = ();
	my $tc = 0;

	print "\nstep $s:\n";

	for $w ((0 - $s) .. (0 + $s)) {
		for $z ((0 - $s) .. (0 + $s)) {
			print "z=$z, w = $w:\n";
			for $x ((0 - $s) .. ($mx + $s)) {
				for $y ((0 - $s) .. ($mx + $s)) {
					my $c = count($x, $y, $z, $w);

					if (defined($w{$x, $y, $z, $w}) && $w{$x, $y, $z, $w} eq '#') {
						$nw{$x, $y, $z, $w} = ($c == 2 || $c == 3) ? '#' : '.';
					} elsif (!defined($w{$x, $y, $z, $w}) || $w{$x, $y, $z, $w} ne '#') {
						$nw{$x, $y, $z, $w} = ($c == 3) ? '#' : '.';
					}

					$tc ++ if $nw{$x, $y, $z, $w} eq '#';
					#					print $nw{$x, $y, $z, $w};
				}
				# print "\n";
			}
		}
	}

	%w = %nw;
	return $tc;
}

