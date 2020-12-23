#!/usr/bin/perl -w

use strict;

my @p1 = ();
my @p2 = ();
my $p2 = 0;
my $w = undef;
my $sg = 0;

while (<>) {
	chomp();
	$p2 = 1 if /^Player 2:/;
	next if /^Player/;
	next unless /\d+/;

	if ($p2) {
		push @p2, $_;
	} else {
		push @p1, $_;
	}
}

my $wc;
($w, $wc) = subgame(\@p1, \@p2);

@p1 = @{$wc};

print "w: @p1\n";

my $out = 0;
while (@p1) {
	$out += scalar(@p1) * (shift @p1);
}

print "$out\n";

sub subgame {
	my %seen = ();
	my @p1 = @{shift @_};
	my @p2 = @{shift @_};
	my $w = undef;

	$sg++;
	my $turn = 0;
	print "Subgame $sg:\n";

	while (scalar(@p1) * scalar(@p2)) {
		$turn ++;
		print "\nturn $turn in game $sg\n";
		print "p1: @p1\n";
		print "p2: @p2\n";
		my $seis = seis(\@p1, \@p2);
		if ($seen{$seis}) {
			print "loop, p1 wins\n";
			$w = 1;
			last;
		}
		$seen{$seis} = 1;


		my $p1 = shift @p1;
		my $p2 = shift @p2;

		if (scalar(@p1) < $p1 || scalar(@p2) < $p2) {
			if ($p1 > $p2) {
				print "p1 wins round ($p1 > $p2)\n";
				push @p1, $p1, $p2;
			} else {
				print "p2 wins round ($p1 > $p2)\n";
				push @p2, $p2, $p1;
			}
		} else {
			my ($ws, undef) = subgame([@p1[0 .. $p1 - 1]], [@p2[0 .. $p2 - 1]]);
			if ($ws == 1) {
				print "p1 wins round (subgame)\n";
				push @p1, $p1, $p2;
			} else {
				print "p2 wins round (subgame)\n";
				push @p2, $p2, $p1;
			}
		}

	}

	$w //= (scalar(@p1) ? 1 : 2);

	print "subgame win: $w\n";
	($w, $w == 1 ? \@p1 : \@p2);
}


sub seis {
	my @s = ();
	push @s, scalar(@{$_[0]});
	push @s, @{$_[0]};
	push @s, scalar(@{$_[1]});
	push @s, @{$_[1]};

	return join($;, @s);
}
