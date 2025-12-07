#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

s = ls[0].index('S')

beams = set()
beams.add(s)
ways = dict()
ways[s] = 1 

splits = 0

def upd(ways, wn, b, bn):
    if bn in wn:
        wn[bn] += ways[b]
    else:
        wn[bn] = ways[b]

for i in range(1, len(ls)):
    bn = set()
    wn = dict()
    for b in beams:
        if ls[i][b] == '.':
            bn.add(b)
            upd(ways, wn, b, b)
        else:
            bn.add(b - 1)
            bn.add(b + 1)
            upd(ways, wn, b, b - 1)
            upd(ways, wn, b, b + 1)
            splits += 1
    beams = bn
    ways = wn

print(splits)
print(sum(ways.values()))
