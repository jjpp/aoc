#!/usr/bin/python3

import sys
from itertools import permutations, tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

ds = {}
cities = set()

for l in sys.stdin:
    [frm, zz, to, zz, dist] = l.strip().split(' ')
    ds[frm, to] = ds[to, frm] = int(dist)
    print(frm, to)
    cities |= set([frm, to])

print(cities)

mind = sum(ds.values())
maxd = 0

for seq in permutations(cities):
    for x in pairwise(seq):
        print(x, ds[x[0], x[1]])
    d = sum([ds[c[0], c[1]] for c in pairwise(seq)])
    print(seq, d)
    mind = min(mind, d)
    maxd = max(maxd, d)

print(mind, maxd)

