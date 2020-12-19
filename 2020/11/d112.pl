#!/usr/bin/perl

@l = <>;
chomp @l;
unshift @l, "." x length($l[0]);
push @l, "." x length($l[0]);
@s = map { ['.', split(''), '.'] } @l;

$r = length($l[0]);
print $r;



do {
	print $c, "\n";
for (@s) {
	print join('', @{$_}), "\n";
}
	@s2 = map { [ @{$_} ] } @s;
	$c = 0;
	for $i (1 .. $#s - 1) {
		for $j (1 .. $r) {
			$c++ if toggle($i, $j);
		}
	}
	@s = @s2;
} while ($c > 0);

$c = 0;
for $i (1 .. $#s - 1) {
	for $j (1 .. $r) {
		$c ++ if ($s[$i] -> [$j] eq '#');
	}
}

print $c, "\n";

sub first {
	my ($i, $j, $dx, $dy) = @_;
	while ($i > 0 && $j > 0 && $i < $#s && $j <= $r) {
		$i += $dx;
		$j += $dy;
		if ($s[$i] -> [$j] eq '#' or $s[$i] -> [$j] eq 'L') {
			return $s[$i] -> [$j];
		}
	}
	return '.';
}

sub toggle {
	my ($i, $j) = @_;
	return 0 if $s[$i] -> [$j] eq '.';

	my $z = (first($i, $j, -1, -1) eq '#') +
		(first($i, $j, -1, -0) eq '#') +
		(first($i, $j, -1, +1) eq '#') +
		(first($i, $j, -0, -1) eq '#') +
		(first($i, $j, -0, +1) eq '#') +
		(first($i, $j, +1, -1) eq '#') +
		(first($i, $j, +1, -0) eq '#') +
		(first($i, $j, +1, +1) eq '#');
	
	if ($s[$i] -> [$j] eq 'L' && $z == 0) {
		$s2[$i] -> [$j] = '#';
		return 1;
	} 

	if ($s[$i] -> [$j] eq '#' && $z > 4) {
		$s2[$i] -> [$j] = 'L';
		return 1;
	}

	return 0;
}
