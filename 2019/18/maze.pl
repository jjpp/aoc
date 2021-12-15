#!/usr/bin/perl -w


use strict;

my %m = ();
my ($X, $Y);
my ($x0, $y0);
my @dx = (1, 0, -1, 0);
my @dy = (0, 1, 0, -1);

my $steps = 0;
my $minsteps = undef;

my %key = ();

while (<>) {
	chomp();
	my ($x, $y) = (0, $. - 1);
	for (split('')) {
		$m{$x, $y} = $_;
		($x0, $y0) = ($x, $y) if $_ eq '@';
		$x ++;
	}
	$X = length($_) - 1;
}

$Y = $. - 1;

$key{'@'} = 1;

printmap();

dfs();

print "$minsteps\n";

sub dfs {
	my @keys = find_next_key();
	my $k;

	if (!scalar(@keys)) {
		if (!defined($minsteps) || $steps < $minsteps) {
			$minsteps = $steps;
			print "new min: $minsteps\n";
		}
		# print "final\n";
		# printmap();
	}

	for $k (@keys) {
		my ($nk, $kl);
		($nk, $x0, $y0, $kl) = @{$k};
		# print "nk = $nk, ($x0, $y0)\n";
		
		next if (defined($minsteps) && $steps + $nk >= $minsteps);
		$steps += $nk;
		for (@{$kl}) {
			$key{$_} = 1;
		}
		
		dfs();
		# print "steps = $steps, ", join(", ", keys %key), "\n";
		# printmap();

		delete ($key{$_}) for (@{$kl});
		$steps -= $nk;
	}
}

sub printmap {
	my ($x, $y);
	for $y (0 .. $Y) {
		for $x (0 .. $X) {
			if (!defined($m{$x, $y})) {
				print "x = $x, y = $y\n";
			}
			if ($x == $x0 && $y == $y0) {
				print "@";
			} else {
				print ($m{$x, $y} =~ /[a-zA-Z\@]/ && $key{lc($m{$x, $y})} ? '.' : $m{$x, $y});
			}
		}
		print "\n";
	}
	print "\n";
}

sub find_next_key {
	my %seen = ();
	$seen{$x0, $y0} = [0, {}];

	my @out = ();

	# print join(", ", (sort (keys %key))), "\n";

	my $c = 0;
	my $s = 0;
	my $d;
	do {
		$c = 0;
		my ($x, $y);
		for $y (0 .. $Y) {
			for $x (0 ..$X) {
				if ((($seen{$x, $y} // []) -> [0] // -1)  == $s) {
					my %lkey = %{$seen{$x, $y} -> [1]};
					my $p = $m{$x, $y};
					if ($p =~ /[a-z]/ && !defined($key{$p}) && !defined($lkey{$p})) {
						$seen{$x, $y} -> [1] -> {$p} = 1;
						$lkey{$p} = 1;
						push @out, [$seen{$x, $y} -> [0], $x, $y, [keys %{$seen{$x, $y} -> [1]}]];
					}

					for $d (0 .. 3) {
						my ($x_, $y_) = ($x + $dx[$d], $y + $dy[$d]);
						if (!blocked($m{$x_, $y_}, \%lkey) && !defined($seen{$x_, $y_})) {
							$seen{$x_, $y_} = [$s + 1, { %lkey } ];
							$c ++;
						}
					}
				}
			}
		}
		$s ++;
	} while($c > 0);

	@out;
}

sub blocked {
	my $x = $_[0];
	my $lkey = $_[1];
	(!defined($x) or $x eq '#' or ($x ge 'A' and $x le 'Z' and !defined($key{lc($x)}) and !defined($lkey -> {lc($x)})));
}
