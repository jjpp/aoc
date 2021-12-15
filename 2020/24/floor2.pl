#!/usr/bin/perl -w

use strict;

my %f = ();

my ($minx, $miny, $maxx, $maxy) = (-1, -1, 1, 1);
my @dx = (1, -1, 1, 0, -1, 0);
my @dy = (0, 0, 1, 1, -1, -1);

while (<>) {
	chomp();
	flip($_);
}

my $p1 = scalar(grep { $_ == 1 } (values %f));

print "$p1\n";

($minx, $miny, $maxx, $maxy) = ($minx - 2, $miny - 2, $maxx + 2, $maxy + 2);

for (1..100) {
	iterate($_);
}

my $p2 = scalar(grep { $_ == 1 } (values %f));

print "$p2\n";



sub iterate {
	my $f = \%f;
	my %nf = ();

	my ($x, $y);
	my ($minx_, $miny_, $maxx_, $maxy_) = ($minx, $miny, $maxx, $maxy);

	print "($minx, $miny, $maxx, $maxy);\n";

	for $y ($miny .. $maxy) {
		for $x ($minx .. $maxx) {
			my $c = count($f, $x, $y);
			print "at $x, $y -> $c\n";
			if ($f -> {$x, $y} // 0 == 1) {
				$nf{$x, $y} = ($c == 0 || $c > 2) ? 0 : 1;
			} else {
				$nf{$x, $y} = ($c == 2) ? 1 : 0;
			}

			$minx_ = $minx_ < ($x - 1) ? $minx_ : ($x - 1);
			$maxx_ = $maxx_ > ($x + 1) ? $maxx_ : ($x + 1);
		}

		$miny_ = $miny_ < ($y - 1) ? $miny_ : ($y - 1);
		$maxy_ = $maxy_ > ($y + 1) ? $maxy_ : ($y + 1);
	}

	%f = %nf;
	($minx, $miny, $maxx, $maxy) = ($minx_, $miny_, $maxx_, $maxy_);
	print "after iteration $_[0]: ", scalar(grep { $_ == 1 } (values %f)), "\n";
}

sub count {
	my ($f, $x, $y) = @_;
	return scalar(grep { $f -> {$x + $dx[$_], $y + $dy[$_]} // 0 == 1; } (0 .. 5));
}


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

	$minx = $minx > $x ? $x : $minx;
	$maxx = $maxx < $x ? $x : $maxx;
	$miny = $miny > $y ? $y : $miny;
	$maxy = $maxy < $y ? $y : $maxy;
}
