#!/usr/bin/python3

import sys
from collections import defaultdict

lns = [l.strip() for l in sys.stdin]

imp = lns.pop(0)
lns.pop(0)

g = defaultdict(lambda: 0)

for r, l in enumerate(lns):
    for c, x in enumerate(l):
        if x == "#":
            g[r, c] = 1

def idx(x, y, g):
    o = 0
    for w in range(y - 1, y + 2):
        for z in range(x - 1, x + 2):
            o *= 2
            o += g[w, z]
    # print(f"{z},{w} -> {o}")
    return o


def it(step, default, g):
    o = defaultdict(lambda: default)
    for x in range(-2*step, len(lns[0]) + 1 + 2*step):
        l = ""
        for y in range(-2*step, len(lns) + 1 + 2*step):
            o[y, x] = 1 if imp[idx(x, y, g)] == "#" else 0
            l += "#" if o[y, x] == 1 else "."
        #print(l)
    #print()
            

    return o

default = 0
for step in range(2):
    default = (1 if imp[0] == "#" else 0) - default
    g = it(step + 1, default, g)

print(sum([x for x in g.values()]))

for step in range(2, 50):
    default = (1 if imp[0] == "#" else 0) - default
    g = it(step + 1, default, g)

print(sum([x for x in g.values()]))





