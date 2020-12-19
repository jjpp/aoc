#!/usr/bin/perl

$s = <>;
chomp $s;

$b = <>;
chomp $b;

@b = split(',', $b);

$min = undef;
$mp = undef;

for (@b) {
	next if $_ eq 'x';
	$n = ((($s % $_) + 1) * $_ - $s) % $_;
	if (!(defined $min) || $n < $min) {
		$min = $n;
		$mp = $_;
	}
	print "$_, $n\n";
}

print $mp * $min, "\n";


