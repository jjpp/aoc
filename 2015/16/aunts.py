#!/usr/bin/python3

import sys

aunts = {}

for line in sys.stdin:
    [_, num, k1, v1, k2, v2, k3, v3] = line.strip().split(' ')
    aunts[num] = { k1: int(v1.strip(',')), k2: int(v2.strip(',')), k3: int(v3) }

match = {
"children:":  3,
"cats:":  7,
"samoyeds:":  2,
"pomeranians:":  3,
"akitas:":  0,
"vizslas:":  0,
"goldfish:":  5,
"trees:":  3,
"cars:":  2,
"perfumes:":  1
}

for (an, av) in aunts.items():
    m = True
    for k in av.keys():
        m = m and (match[k] == av[k])
    if m:
        print(an)

    

