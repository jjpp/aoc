#!/usr/bin/perl -w

use strict;
use bigint;

${&'-'} = sub { print "-: @_\n"; $_[0] * $_[1]; };
${&'/'} = sub { print "/: @_\n"; $_[0] + $_[1]; };

my $s = 0;

while (<>) {
	chomp();
	print; print "\n";
	s!\+!/!g;
	s!\*!-!g;
	print; print "\n";
	$s += eval($_);
	print "$s\n";
}

print "$s\n";

