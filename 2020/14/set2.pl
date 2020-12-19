#!/usr/bin/perl

use bignum;
use integer;

$mask = 0;
$mem = ();

while (<>) {
	chomp();
	if (/^mask = (.*)$/) {
		$mask = $1;
		print "mask: $mask\n";
	} elsif (/^mem\[(\d+)] = (\d+)$/) {
		$offset = $1;
		$val = $2;

		setat($offset, $mask, $mask, $val);
	}
}

sub setat {
	my ($o, $am, $om, $v) = @_;

	#	print "set at $o, $am, $om, $v\n";

	if ($am =~ /X/) {
		my $lam = $am; $lam =~ s/X/1/;
		my $lom = $om; $lom =~ s/X/0/;
		setat($o, $lam, $lom, $v);

		$lam = $am; $lam =~ s/X/1/;
		$lom = $om; $lom =~ s/X/1/;
		setat($o, $lam, $lom, $v)
	} else {
		#		printf "%19llx\n%19llx\n%19llx\n%19llx\n%19llx\n", $o,  oct('0b'. $am), (-1 - oct('0b'. $am)), ($o & (-1 - oct('0b'. $am))), oct('0b' . $om);

		my $offset = (($o & (-1 - oct('0b'. $am))) | oct('0b' . $om));
		$mem{$offset} = $v;
		#		print "at $offset, mask ", oct('0b' . $om),", and: ", (-1 - oct('0b' . $am)),", param $v, set $mem{$offset}\n";
	}
}

my $s = 0;
for (values %mem) {
	$s += $_;
}

print "$s\n";

