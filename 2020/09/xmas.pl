#!/usr/bin/perl

$pa = shift @ARGV;

@s = ();
@min = ();
@max = ();

@q = ();
$w = undef;

while (<>) {
	chomp();
	my $n = $_;

	push @s, [$n];
	push @min, [$n];
	push @max, [$n];

	for (0 .. $#s - 1) {
		push @{$s[$_]}, $s[$_] -> [-1] + $n;
		push @{$min[$_]}, ($min[$_] -> [-1] < $n ? $min[$_] -> [-1] : $n);
		push @{$max[$_]}, ($max[$_] -> [-1] > $n ? $max[$_] -> [-1] : $n);
	}

	push @q, $n;

	if (scalar(@q) <= $pa || defined($w)) {
	} else {
		print "$n: \n" if $debug;
		my $found = 0;
		for $i (0 .. $pa - 2) {
			last if $found;
			for $j (($i + 1)  .. $pa - 1) {
				print "  $q[$i] $q[$j] -> ", $q[$i] + $q[$j], "\n" if $debug;
				$found = ($q[$i] + $q[$j]) == $n;
				last if $found;
			}
		}
		if (!$found) {
			$w = $n;
			print "weakness: $w\n";
		}
		shift @q;
	}
}

print scalar(@s), "\n" if $debug;

for $i (0 .. $#s) {
	if ($debug) {
		print "i = $i: @{$s[$i]}.\n";
		print "i = $i: @{$min[$i]}.\n";
		print "i = $i: @{$max[$i]}.\n";
	}
	for $j (1 .. $#{$s[$i]}) {
		if ($debug) {
			print "  j = $j\n";
			print "    sum: $s[$i]->[$j]\n";
		}
		if ($s[$i] -> [$j] == $w) {
			if ($debug) {
				print "      $min[$i]->[$j]\n";
				print "      $max[$i]->[$j]\n";
			}
			print ($min[$i]->[$j] + $max[$i]->[$j], "\n");
			exit;
		}
	}
}

