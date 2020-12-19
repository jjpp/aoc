#!/usr/bin/perl

my $c = 0;

my %f = ();

@r = qw( byr iyr eyr hgt hcl ecl pid);

%v = (

#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
	'byr' => sub { local $_ = $_[0]; /^\d\d\d\d$/ && ($_ >= 1920 && $_ <= 2002 ) },
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	'iyr' => sub { local $_ = $_[0]; /^\d\d\d\d$/ && ($_ >= 2010 && $_ <= 2020 ) },
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	'eyr' => sub {local $_ = $_[0];  /^\d\d\d\d$/ && ($_ >= 2020 && $_ <= 2030 ) },
#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
	'hgt' => sub { local $_ = $_[0]; (/^(\d+)cm$/ && ($1 >= 150 && $1 <= 193)) || (/^(\d+)in$/ && ($1 >= 59 && $_ <= 76)) },
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	'hcl' => sub { local $_ = $_[0]; /^#[0-9a-f]{6}$/ },
#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	'ecl' => sub { local $_ = $_[0]; /^(amb|blu|brn|gry|grn|hzl|oth)$/ },
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
	'pid' => sub { local $_ = $_[0]; /^\d{9}$/ },
#    cid (Country ID) - ignored, missing or not.
);


# byr: .* ecl: .* eyr: .* hcl: .* hgt: .* iyr: .* pid: .*


while (<>) {
	chomp();
	if (!$_) {
		proc();
	} else {
		my %d = map { @f = split(':', $_, 2); @f; } (split(' ', $_));
		for (keys %d) { $f{$_} = $d{$_}; }
	}
}

proc();

print $c, "\n";


sub proc {
		print join(" ", map { "$_:$f{$_}" } (sort keys %f)), "\n";
		for (@r) {
			if (!defined($f{$_}) || !($v{$_}($f{$_}))) {
				print "fail at $_\n";
				goto fail;
			}
		}

		$c ++;
		fail:
		%f = ();
}

