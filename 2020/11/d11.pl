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



sub toggle {
	my ($i, $j) = @_;
	return 0 if $s[$i] -> [$j] eq '.';

	my $z = ($s[$i - 1]->[$j - 1] eq '#') + 
		($s[$i - 1]->[$j - 0] eq '#') +
		($s[$i - 1]->[$j + 1] eq '#') +
		($s[$i - 0]->[$j - 1] eq '#') +
		($s[$i - 0]->[$j + 1] eq '#') +
		($s[$i + 1]->[$j - 1] eq '#') +
		($s[$i + 1]->[$j - 0] eq '#') +
		($s[$i + 1]->[$j + 1] eq '#');
	
	if ($s[$i] -> [$j] eq 'L' && $z == 0) {
		$s2[$i] -> [$j] = '#';
		return 1;
	} 

	if ($s[$i] -> [$j] eq '#' && $z > 3) {
		$s2[$i] -> [$j] = 'L';
		return 1;
	}

	return 0;
}
