#!/usr/bin/perl


$min = 1000000000;
$max = 0;
%p = ();

while (<>) {
	chomp();
	print;
	s/[FL]/0/g;
	s/[BR]/1/g;
	$id = decode($_);
	print " $_ $id\n";
	$max = $id if $id > $max;
	$min = $id if $id < $min;
	$p{$id} = 1;
}

print "$max\n";

for ($min .. $max) {
	print "$_\n" if (!$p{$_});
}


sub decode {
	my $out = 0;
	for (split('', $_[0])) {
		$out *= 2;
		$out ++ if $_;
	}
	$out;
}
