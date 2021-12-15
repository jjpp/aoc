#!/usr/bin/python3

import sys
from itertools import *

lns = [l.strip() for l in sys.stdin]

src = lns.pop(0)
lns.pop(0)

pairs = {}
for l in lns:
    (p, v) = l.split(' -> ')
    pairs[p] = [p[0] + v, v + p[1]]

print(pairs)


pc = {}

print(src)

for (a, b) in  zip(src, src[1:] + " "):
    pc[a+b] = pc.get(a+b, 0) + 1

def it(pc):
    out = { **pc }
    print(out, sum(out.values()))
    for p in pc.keys():
        if p in pairs and pc[p] > 0:
            print(p, " -> ", pairs[p])
            out[p] -= pc[p]
            out[pairs[p][0]] = out.get(pairs[p][0], 0) + pc[p]
            out[pairs[p][1]] = out.get(pairs[p][1], 0) + pc[p]
    return out
            
for _ in range(40):
    pc = it(pc)

c = {}
for x in pc.keys():
    c[x[0]] = c.get(x[0], 0) + pc[x]

print(c)

print(max(c.values()) - min(c.values()))

