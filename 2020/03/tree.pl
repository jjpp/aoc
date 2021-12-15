#!/usr/bin/perl


$p = 0;
$c = 0;

while (<>) {
	chomp();
	my @d = split('', $_);
	my $l = scalar(@d);
	$c++ if ($d[$p % $l] eq "#");
	$d[$p % $l] = ($d[$p % $l] eq "#") ? 'X' : 'O';
	print join('', @d), "\n";
	$p += 3;
}

print $c, "\n";



