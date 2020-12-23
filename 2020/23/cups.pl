#!/usr/bin/perl -w

use strict;

my $c = <>;
chomp $c;
my @c = split '', $c;

for (1 .. 100) {
	@c = move(\@c);
}

print "final: @c\n";

while ($c[0] ne 1) { 
	push @c, shift @c;
}

shift @c;

print @c, "\n";



sub move {
	my @c = @{shift @_};
	print "before: @c\n";

	my $current = $c[0];

	my @pu = @c[1, 2, 3];
	splice(@c, 1, 3);

	my $d = $current - 1;

	while (!scalar(grep { $_ == $d } @c)) {
		$d --;
		$d = 9 if ($d < 1);
	}
	
	my $pos = 0;
	while ($c[$pos] ne $d) { $pos ++ }
	splice @c, $pos + 1, 0, @pu;

	push @c, shift @c;

	return @c;
}


