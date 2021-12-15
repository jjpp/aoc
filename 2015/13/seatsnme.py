#!/usr/bin/python3

import sys
from itertools import permutations, tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

ds = {}
guests = set()

for l in sys.stdin:
    [a, _w, gl, p, _h, _u, _b, _s, _n, _t, b] = l.strip().split(' ')
    b = b.strip('.')
    ds[a, b] = int(p) * (1 if gl == 'gain' else -1)
    guests |= set([a, b])

for g in guests:
    ds[g, 'Me'] = ds['Me', g] = 0

guests |= set(['Me'])

maxd = 0

for seq in permutations(guests):
    d = sum([ds[c[0], c[1]] + ds[c[1], c[0]] for c in pairwise(seq)]) + ds[seq[0], seq[-1]] + ds[seq[-1], seq[0]]
    print(seq, d)
    maxd = max(maxd, d)

print(maxd)

