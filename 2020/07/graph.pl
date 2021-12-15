#!/usr/bin/perl

%in = ();

while (<>) {
	chomp();

	$_ =~ /^(.*) bags contain (.*)\.$/;
	my $k = $1;
	for (split(', ', $2)) {
		/^\d+ (.*) bags?$/ or next;
		if (ref($in{$1}) ne 'HASH') {
			$in{$1} = {};
		}
		${$in{$1}}{$k} = 1;
	}
}

my %seen = ();
my @scan = ('shiny gold');
my $count = 0;

while (@scan) {
	$k = shift @scan;
	next if $seen{$k};
	$seen{$k} = 1;
	$count ++;
	print "Considering $k: ", join(', ', keys %{$in{$k}}), "\n";
	for $j (keys %{$in{$k}}) {
		if (!$seen{$j}) {
			print "Can be in $j.\n";
			push @scan, $j;
		}
	}
}

print $count - 1, "\n";

