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
	my @p = ();

	($r, $e) = getvalue($e);

	oploop:
	while (scalar(@{$e})) {
		my ($op, $v2);
		($op, $e) = getop($e);
		($v2, $e) = getvalue($e);

		print "op = $op, $v2 = $v2\n";

		if ($op eq '*') {
			print "push $r\n";
			push @p, $r;
			$r = $v2;
		} elsif ($op eq '+') {
			print "$r + $v2\n";
			$r = $r + $v2;
		} else {
			print "unknown operator: $op\n";
		}
	}

	push @p, $r;
	print "p = @p\n";

	my $o = shift @p;
	for (@p) {
		$o *= $_;
	}

	return $o;
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
