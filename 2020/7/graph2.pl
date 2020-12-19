#!/usr/bin/perl

%in = ();

while (<>) {
	chomp();

	$_ =~ /^(.*) bags contain (.*)\.$/;
	my $k = $1;
	$in{$k} = {};

	for (split(', ', $2)) {
		/^(\d+) (.*) bags?$/ or next;
		${$in{$k}}{$2} = $1;
	}
}

my %seen = ();
my $count = 0;

my %c = ();

for (keys %in) {
	if (!scalar(keys(%{$in{$_}}))) {
		push @scan, $_;
		$c{$_} = 1;
	}
}

for (keys %c) {
	print "$_ => $c{$_}\n";
}


while (@scan) {
	$k = shift @scan;

	print "scanning $k\n";

	for $j (keys %in) {
		next if $seen{$j};
		print "checking if $j contains all ", join(', ', keys %{$in{$j}}),"\n";
		next if grep { !defined($c{$_}) } keys %{$in{$j}};
		print "it does\n";
		my $sum = 1;
		for (keys %{$in{$j}}) {
			$sum += $in{$j}{$_} * $c{$_};
		}
		$c{$j} = $sum;
		print "in $j $sum bags\n";
		$seen{$j} = 1;
		push @scan, grep { !$seen{$_} } (keys %{$in{$j}});
	}
}

for (keys %c) {
	print "$_ => $c{$_}\n";
}

print $c{'shiny gold'} - 1, "\n";


