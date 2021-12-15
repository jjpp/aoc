#!/usr/bin/python3

import sys

aunts = {}

for line in sys.stdin:
    [_, num, k1, v1, k2, v2, k3, v3] = line.strip().split(' ')
    aunts[num] = { k1: int(v1.strip(',')), k2: int(v2.strip(',')), k3: int(v3) }

match = {
"children:": lambda x: x == 3,
"samoyeds:": lambda x: x == 2,
"akitas:": lambda x: x == 0,
"vizslas:": lambda x: x == 0,
"cars:": lambda x: x == 2,
"perfumes:": lambda x: x == 1,

"pomeranians:": lambda x: x < 3,
"goldfish:": lambda x: x < 5,

"cats:": lambda x: x > 7,
"trees:": lambda x: x > 3,
}

for (an, av) in aunts.items():
    m = True
    for k in av.keys():
        m = m and (match[k](av[k]))
    if m:
        print(an)

    

