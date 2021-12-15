#!/usr/bin/perl



%y = ();
$c = 0;
$g = 0;
$call = 0;

while (<>) {
	chomp();
	if ($_) {
		for (split('', $_)) {
			$y{$_} = $y{$_} + 1;
		}
		$g ++;
	} else {
		proc();
	}
}
proc();

sub proc {
	$c += scalar (keys %y);
	$call += scalar (grep { $y{$_} == $g } (keys %y));
	%y = ();
	$g = 0;
}

print "$c\n";
print "$call\n";

