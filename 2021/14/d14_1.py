#!/usr/bin/python3

import sys
from itertools import *

lns = [l.strip() for l in sys.stdin]

src = lns.pop(0)
lns.pop(0)

pairs = {}
for l in lns:
    (p, v) = l.split(' -> ')
    pairs[p] = v

print(pairs)

def it(x):
    out = x[0]
    for (a, b) in  zip(x, x[1:]):
        if a+b in pairs:
            out += pairs[a+b] 
        out += b
    return out

for _ in range(10):
    src = it(src)
    print(src)

c = {}
for x in src:
    c[x] = c.get(x, 0) + 1

print(max(c.values()) - min(c.values()))

