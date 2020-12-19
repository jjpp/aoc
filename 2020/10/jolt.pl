#!/usr/bin/perl

@jolts = sort { $a <=> $b } (<>);

unshift @jolts, 0;
push @jolts, $jolts[$#jolts] + 3;

@d = ();
@d2 = ();
for (1 .. $#jolts) {
	$d[$jolts[$_] - $jolts[$_ - 1]] ++;
	$d2[$_] = $jolts[$_] - $jolts[$_ - 1];
}

print "$d[1] $d[3] ", ($d[1] * $d[3]), "\n";

@w = (1);

for (1 .. $#jolts) {
	@w[$_] = $w[$_ - 1] 
		+ (($_ > 1 && ($d2[$_] + $d2[$_ - 1]) <= 3) ? $w[$_ - 2] : 0)
		+ (($_ > 2 && ($d2[$_] + $d2[$_ - 1] + $d2[$_ - 2]) <= 3) ? $w[$_ - 3] : 0);
}

print $w[$#jolts], "\n";

