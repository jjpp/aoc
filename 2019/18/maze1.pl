#!/usr/bin/perl -w


use strict;

my %m = ();
my ($X, $Y);
my ($x0, $y0);
my @dx = (1, 0, -1, 0);
my @dy = (0, 1, 0, -1);

my %dist = (); # key -> key2 -> [ dist, [ keys needed ] ];
my %keys = ();

my $minsteps = undef;

while (<>) {
	chomp();
	my ($x, $y) = (0, $. - 1);
	for (split('')) {
		$m{$x, $y} = $_;
		$keys{$_} = [$x, $y] if /[a-z@]/;
		$x ++;
	}
	$X = length($_) - 1;
}

$Y = $. - 1;

print scalar(keys %keys) - 1, " keys to be found\n";

for (keys %keys) {
	$dist{$_} = find_distances(@{$keys{$_}});
}

printmap(@{$keys{'@'}});

my $notfound = { map { $_ => 1 } (keys %keys) };
delete $notfound -> {'@'};

#dfs(0, ['@'], $notfound);
bfs();

print "$minsteps\n";

sub bfs {
	my %m = ();

	$m{'@', 0, ''} = [0, {}, ['@']];

	my @upd = ('@' . $; . 0 . $;);

	while (@upd) {
		@upd = sort { (keys %{$m{$b} -> [1]}) <=> (keys %{$m{$a} -> [1]}) || $m{$a} -> [0] <=> $m{$b} -> [0] } @upd;
		my ($from, $kc, $seen) = split($;, shift @upd);
		my $to;
		my $steps = $m{$from, $kc, $seen} -> [0];
		my $keys = $m{$from, $kc, $seen} -> [1];
		my @path = @{$m{$from, $kc, $seen} -> [2]};

		print "considering $from, $kc: $steps, keys seen: ", join(", ", sort (keys %{$keys})), " (@path)\n";

		for $to (keys %keys) {
			next if $to eq '@';
			next if $keys -> {$to};

			print "  checking $to ($kc + 1):\n";

			my @missing = grep { !$keys -> {$_} } @{$dist{$from} -> {$to} -> [1]};
			if (@missing) {
				print "   missing keys: @missing\n";
				next;
			}

			my $newseen = join("", sort { $a cmp $b } (keys %{$keys}, $to));

			print "    not seen before\n" if !defined($m{$to, $kc + 1, $newseen});
			if (defined($m{$to, $kc + 1, $newseen})) {
				print "    previous keyset: ", join(", ", keys %{$m{$to, $kc + 1, $newseen} -> [1]}), "\n";
				print "    dist: ", $dist{$from} -> {$to} -> [0], "\n";
				print "    prev steps: $m{$to, $kc + 1, $newseen}->[0]\n";
			}

			if (!defined($m{$to, $kc + 1, $newseen}) || 
				($steps + $dist{$from} -> {$to} -> [0] < $m{$to, $kc + 1, $newseen} -> [0])) {
				$m{$to, $kc + 1, $newseen} = [ $steps + $dist{$from} -> {$to} -> [0], { %{$keys}, $to => 1 }, [@path, $to] ];
				print "    steps now: $m{$to, $kc + 1, $newseen}->[0]\n";
				print "    keys seen now: ", join(", ", sort(keys %{$m{$to, $kc + 1, $newseen} -> [1]})), "\n";
				if (($kc + 1) == scalar(keys %keys) - 1) {
					$minsteps = ($minsteps // 100000000) > $m{$to, $kc + 1, $newseen} -> [0]
						? $m{$to, $kc + 1, $newseen} -> [0] : $minsteps;
					print "    new minsteps: $minsteps\n";
				}
				push @upd, $to . $; . ($kc + 1) . $; . $newseen;
			}
		}
	}

	for (sort { scalar(keys %{$m{$a} -> [1]}) <=> scalar(keys %{$m{$b} -> [1]}) }  (keys %m)) {
		print "$_: $m{$_}->[0]: ", join(", ", sort(keys %{$m{$_} -> [1]})), ": @{$m{$_} -> [2]}\n";
	}

}

sub dfs {
	my $steps = shift @_;
	my $found = shift @_;
	my $notfound = shift @_;
	my $this = $found -> [$#{$found}];

	if (!scalar(keys %{$notfound})) {
		if (!defined($minsteps) or $steps < $minsteps) {
			$minsteps = $steps;
			print "found: $minsteps: @{$found}\n";
		}
		return;
	} 

	if (defined($minsteps) && ($steps >= $minsteps)) {
		#print "cut at @{$found}\n";
		return;
	}

	my $k;
	for $k (sort { $dist{$this} -> {$a} -> [0] <=> $dist{$this} -> {$b} -> [0] } (keys %{$notfound})) {
		next if scalar(grep { $notfound -> {$_} } @{$dist{$this} -> {$k} -> [1]});
		my %nf2 = %{$notfound};
		delete %nf2{$k};
		push @{$found}, $k;
		dfs($steps + $dist{$this} -> {$k} -> [0], $found, \%nf2);
		pop @{$found};
	}
}


sub printmap {
	my ($x0, $y0) = @_;
	my ($x, $y);
	for $y (0 .. $Y) {
		for $x (0 .. $X) {
			if (!defined($m{$x, $y})) {
				print "undefined: x = $x, y = $y\n";
			}
			print $m{$x, $y};
		}
		print "\n";
	}
	print "\n";
}

sub find_distances {
	my ($x0, $y0) = @_; 
	my %seen = ();
	$seen{$x0, $y0} = [0, {}];
	my %dist = ();

	my $c = 0;
	my $s = 0;
	my $d;
	do {
		$c = 0;
		my ($x, $y);
		for $y (0 .. $Y) {
			for $x (0 ..$X) {
				if ((($seen{$x, $y} // []) -> [0] // -1)  == $s) {
					my %lkey = %{($seen{$x, $y} // []) -> [1]};

					if ($m{$x, $y} =~ /[A-Z]/) {
						$lkey{lc($m{$x, $y})} = 1;
						$seen{$x, $y} -> [1] -> {lc($m{$x, $y})} = 1;
					}

					if ($m{$x, $y} =~ /[a-z]/) {
						$dist{$m{$x, $y}} = [ $s, [ keys %lkey ] ];
					}

					for $d (0 .. 3) {
						my ($x_, $y_) = ($x + $dx[$d], $y + $dy[$d]);
						if ($m{$x_, $y_} ne '#'  && !defined($seen{$x_, $y_})) {
							$seen{$x_, $y_} = [$s + 1, { %lkey } ];
							$c ++;
						}
					}
				}
			}
		}
		$s ++;
	} while($c > 0);

	\%dist;
}

