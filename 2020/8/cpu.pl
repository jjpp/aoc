#!/usr/bin/perl


@code = map { chomp; [split(' ', $_)]; } (<>);

%seen = ();
%stops = ();

$ip = 0;
$acc = 0;
@t = ();
@a = ();

while (!$seen{$ip}) {
	$seen{$ip} = 1;
	push @t, $ip;
	push @a, $acc;
	if ($code[$ip] -> [0] eq 'acc') {
		$acc += $code[$ip] -> [1];
		$ip ++;
	} elsif ($code[$ip] -> [0] eq 'jmp') {
		$ip += $code[$ip] -> [1];
		$badjmp{$_} = 1;
	} else {
		$ip ++;
	}
}

print "$acc\n";

print "@t\n";

do {
	$found = 0;

	for (0 .. $#code) {
		next if $stops{$_};
		my $next = ($code[$_] -> [0] eq 'jmp') ? $_ + $code[$_] -> [1] : $_ + 1;
		if ($next > $#code || $stops{$next}) {
			print "$_ stops\n";
			$stops{$_} = 1;
			$found ++;
		}
	}
} while $found > 0;


my $fix = -1;


for (0 .. $#code) {
	print "$_: @{$code[$_]} seen:$seen{$_} seennxt:$seen{$_ + 1} seenprm:$seen{$_ + $code[$_] -> [1]} badjmp:$badjmp{$_}\n";
	next unless $seen{$_};
	print "seen\n";
	next if $code[$_] -> [0] eq 'acc';
	print "!acc\n";
	my $next = $code[$_] -> [0] eq 'nop' ? $_ + $code[$_] -> [1] : $_ + 1;
	next unless $stops{$next};

	print "fix $_\n";
	$fix = $_;
	last;
}

print "fix $fix\n";

$code[$fix] = [($code[$fix] -> [0] eq 'nop') ? 'jmp' : 'nop', $code[$fix] -> [1]];
print "@{$code[$fix]}\n";

$acc = 0;
$ip = 0;

while ($ip < scalar(@code)) {
	if ($code[$ip] -> [0] eq 'acc') {
		$acc += $code[$ip] -> [1];
		$ip ++;
	} elsif ($code[$ip] -> [0] eq 'jmp') {
		$ip += $code[$ip] -> [1];
	} else {
		$ip ++;
	}
}

print "$acc\n";

