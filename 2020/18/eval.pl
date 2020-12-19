#!/usr/bin/perl -w

use strict;

my $s = 0;

while (<>) {
	chomp();

	my $r = evalf(split('', $_));
	$s += $r;
}

print "$s\n";

sub evalf {
	my $e = [@_];
	my $r;

	($r, $e) = getvalue($e);

	while (scalar(@{$e})) {
		my ($op, $v2);
		($op, $e) = getop($e);
		($v2, $e) = getvalue($e);

		if ($op eq '*') {
			$r = $r * $v2;
		} elsif ($op eq '+') {
			$r = $r + $v2;
		} else {
			print "unknown operator: $op\n";
		}
	}

	return $r;
}

sub getop {
	my @e = @{shift @_};
	while (scalar(@e) && $e[0] eq ' ') {
		shift @e;
	}
	
	return (shift @e, [@e]);
}

sub getvalue {
	my $v = undef;
	my @e = @{shift @_};

	while (scalar(@e) && $e[0] eq ' ') {
		shift @e;
	}

	if ($e[0] eq '(') {
		shift @e;
		my $pd = 0;
		my @sub = ();
		while (scalar(@e) && ($pd > 0 || $e[0] ne ')')) {
			my $e = shift @e;
			push @sub, $e;
			$pd ++ if $e eq '(';
			$pd -- if $e eq ')';
		}
		shift @e;

		$v = evalf(@sub);
	} elsif ($e[0] =~ /\d+/) {
		$v = shift @e;
		while (scalar(@e) && $e[0] =~ /\d+/) {
			$v *= 10 + (shift @e);
		}
	} else {
		print "not a value: @e\n";
		exit;
	}

	return ($v, [@e]);
}
