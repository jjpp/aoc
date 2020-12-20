#!/usr/bin/perl -w

use strict;
use integer;

my $shift = shift @ARGV;

my %tiles = ();

my $tileid = undef;
my @lines = ();
my %sides = ();
my %flip = ();
while (<>) {
	chomp();
	if (/^Tile (\d+):$/) {
		$tileid = $1;
		$tiles{$tileid} = [];
		$sides{$tileid} = [];
		next;
	}

	if (/^.+$/) {
		if (!scalar(@{$sides{$tileid}})) {
			$sides{$tileid} -> [1] = $_;
		}
		$sides{$tileid} -> [0] = substr($_, $[, 1) . ($sides{$tileid} -> [0] // "");
		$sides{$tileid} -> [2] .= substr($_, -1, 1);
		$sides{$tileid} -> [3] = scalar(reverse $_);
		push @{$tiles{$tileid}}, $_;
	}
}

for (keys %sides) {
	$flip{$_} = [ 
		scalar(reverse $sides{$_} -> [2]),
		scalar(reverse $sides{$_} -> [1]),
		scalar(reverse $sides{$_} -> [0]),
		scalar(reverse $sides{$_} -> [3])
	];
}

my $tiles = scalar(keys %tiles);
my @tiles = sort (keys %tiles);

for (1 .. $shift) { push @tiles, shift @tiles };

my $s = sqrt($tiles);

my @pos = ();
my @dir = ();


pick(\@pos, \@dir, 0);

my $maxp = 0;

sub pick {
	my ($pos, $dir, $p) = @_;

	if ($p > $maxp) {
		print "at $p\n";
		$maxp = $p;
	}

	if ($p >= $tiles) {
		print $pos -> [0] * $pos -> [$s - 1] * $pos -> [$#tiles] * $pos -> [$#tiles + 1 - $s], "\n";
		return 1;
	}

	my $d;
	my $up = ($p >= $s) ? down($pos -> [$p - $s], $dir -> [$p - $s]) : undef;
	my $left = ($p % $s) ? right($pos -> [$p - 1], $dir -> [$p - 1]) : undef;
	my $pick;
	for $pick (@tiles) {
		next if scalar(grep { $_ eq $pick } @pos);
		push @{$pos}, $pick;
		for $d (0 .. 7) {
			next if defined($left) && ($left ne left($pick, $d));
			next if defined($up) && ($up ne up($pick, $d));
			push @{$dir}, $d;
			return 1 if pick($pos, $dir, $p + 1);
			pop @{$dir};
		}
		pop @{$pos};
	}

	return 0;
}

my %pict = ();
my @bits = ();
my $SL = undef;

my $p;
for $p (0 .. $#tiles) {
	print "at $p is $pos[$p] ($dir[$p])\n";
	my @lines = @{$tiles{$pos[$p]}};
	print (substr($_, 1, length($_) - 2), "\n") for @lines[1 .. $#lines - 1];

	if ($dir[$p] > 3) {
		# flip
		print "flip $p ($dir[$p])\n";
		@lines = map { scalar(reverse) } @lines;
		print "---\n";
		print (substr($_, 1, length($_) - 2), "\n") for @lines[1 .. $#lines - 1];
	}
	if ($dir[$p] % 2 > 0) {
		print "rot $p ($dir[$p])\n";
		my ($x, $y);
		my @l = ();
		for $x (0 .. $#lines) {
			for (@lines) {
				$l[$x] .= substr($_, $#lines - $x, 1);
			}
		}
		@lines = @l;
		print "---\n";
		print (substr($_, 1, length($_) - 2), "\n") for @lines[1 .. $#lines - 1];
	}
	if ($dir[$p] % 4 >= 2) {
		print "rot180 $p ($dir[$p])\n";
		@lines = reverse ( map { scalar(reverse) } @lines );
		print "---\n";
		print (substr($_, 1, length($_) - 2), "\n") for @lines[1 .. $#lines - 1];
	}
	print "---\n";
	print (substr($_, 1, length($_) - 2), "\n") for @lines[1 .. $#lines - 1];

	my ($x, $y);
	my $sl = $#lines - 1;
	$SL = $sl unless defined $SL;
	my ($X, $Y) = ($p % $s, $p / $s);
	# print "tile at $X, $Y\n";
	my $bitp;
	for $y (0 .. $#lines - 2) {
		for $x (0 .. $#lines - 2) {
			my ($x_, $y_) = ($X * $sl + $x, $Y * $sl + $y);
			# print "  pixel at $x_, $y_ is ";
			$bitp = $y_ * $sl + $x_;
			$bits[$bitp] = substr($lines[$y + 1], $x + 1, 1);
			# print "'$bits[$bitp]'\n";
			$pict{$x_, $y_} = $bits[$bitp];
		}
	}
}

my %monsters = ();

#                   # 
# #    ##    ##    ###
#  #  #  #  #  #  #   

my @monster = map { [ split('') ] } ((
	'                  # ',
	'#    ##    ##    ###',
	' #  #  #  #  #  #   '
));

checkm([@monster]);
checkm([reverse @monster]);

@monster = map { [ reverse @{$_} ] } @monster;

checkm([@monster]);
checkm([reverse @monster]);

@monster = map { [ split('') ] } ((
	' # ',
	'#  ',
	'   ',
	'   ',
	'#  ',
	' # ',
	' # ',
	'#  ',
	'   ',
	'   ',
	'#  ',
	' # ',
	' # ',
	'#  ',
	'   ',
	'   ',
	'#  ',
	' # ',
	' ##',
	' # ',
));

checkm([@monster]);
checkm([reverse @monster]);

@monster = map { [ reverse @{$_} ] } @monster;

checkm([@monster]);
checkm([reverse @monster]);

my $out = scalar(grep { $_ eq '#' } (values %pict)) - scalar(values %monsters);
print "roughness: $out\n";

my ($x, $y);
for $y (0 .. $SL * $s - 1) {
	for $x (0 .. $SL * $s - 1) {
		print $monsters{$x, $y} // $pict{$x, $y};
	}
	print "\n";
}

sub checkm {
	my $m = shift @_;

	my ($x, $y);
	my ($mx, $my);
	my $ll = $s * $SL - 1;
	for $y (0 .. ($ll - $#{$m})) {
		point:
		for $x (0 .. $ll - $#{$m -> [0]}) {
			for $my (0 .. $#{$m}) {
				for $mx (0 .. $#{$m -> [0]}) {
					next point if $m -> [$my] -> [$mx] eq '#' && $pict{$x + $mx, $y + $my} ne '#';
				}
			}

			for $my (0 .. $#{$m}) {
				for $mx (0 .. $#{$m -> [0]}) {
					$monsters{$x + $mx, $y + $my} = 'O' if $m -> [$my] -> [$mx] eq '#';
				}
			}

		}
	}
}






#  rot	up	right	down	left
#  0  	1	2	3r	0r
#  1	2	3	0r	1r
#  2	3	0	1r	2r
#  3	0	1	2r	3r	

sub dir {
	my ($tile, $rot, $dir) = @_;
	my $sides = ($rot > 3) ? $flip{$tile} : $sides{$tile};
	my $side = $sides -> [($rot + $dir) % 4];
	$side = reverse ($side) if ($dir == 3 || $dir == 0); 
	return $side;
}

sub up { dir(@_[0, 1], 1); }
sub right { dir(@_[0, 1], 2); }
sub down { dir(@_[0, 1], 3); }
sub left { dir(@_[0, 1], 0); }

