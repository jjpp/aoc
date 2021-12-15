#!/usr/bin/perl


$p = 0;
@c = (0, 0, 0, 0, 0);
$r = 0;

while (<>) {
	print;
	chomp();
	my @d = split('', $_);
	my $l = scalar(@d);
	$c[0]++ if ($d[($r * 1) % $l] eq "#");
	$c[1]++ if ($d[($r * 3) % $l] eq "#");
	$c[2]++ if ($d[($r * 5) % $l] eq "#");
	$c[3]++ if ($d[($r * 7) % $l] eq "#");
	if (!($r % 2)) {
		$c[4]++ if ($d[($r / 2) % $l] eq "#");
		$d[($r / 2) % $l] = ($d[($r / 2) % $l] eq "#") ? 'X' : 'O';
	}


	print join('', @d), "\n";

	$r ++;	
}

print "@c\n";

my $c = 1;
for (@c) { $c = $c * $_; }
print $c, "\n";


