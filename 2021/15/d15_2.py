#!/usr/bin/python3

import sys

lns = [l.strip() for l in sys.stdin]

g = {}
Y = len(lns)
X = len(lns[0])

def w(c, i):
    return (int(c) - 1 + i) % 9 + 1

for (row, l) in enumerate(lns):
    for (pos, c) in enumerate(l):
        for dx in range(5):
            for dy in range(5):
                g[pos + dx * X, row + dy * Y] = w(c, dx + dy)

def nrs(p):
    return [(p[0] + dx, p[1] + dy) for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] if (p[0] + dx, p[1] + dy) in g]

s = {}
s[0, 0] = 0
ss = set([(0, 0)])

while (len(ss) > 0):
    so = set()
    for p in ss:
        for pn in nrs(p):
            if not pn in s or s[p] + g[pn] < s[pn]:
                s[pn] = s[p] + g[pn]
                so |= set([pn])
    ss = so


print(s[X * 5 - 1, Y * 5 - 1])
    
