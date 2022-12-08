#!/usr/bin/python3

import sys
from collections import defaultdict

ls = [l.strip() for l in sys.stdin]

Y = len(ls)
X = len(ls[0])

g = {}
ss = {}
h = defaultdict(lambda: -1)

for y in range(0, Y):
    r = ls.pop(0)
    for x in range(0, X):
        c = tuple([x, y])
        g[c] = int(r[x])


check = set()
visible = set()

check.add( tuple([0, 0]) )

UP = tuple([0, -1])
DOWN = tuple([0, 1])
LEFT = tuple([-1, 0])
RIGHT = tuple([1, 0])
dirs = [UP, DOWN, LEFT, RIGHT]

def addcoord(c, d):
    return tuple([c[0] + d[0], c[1] + d[1]])


for y in range(0, Y):
    for x in range(0, X):
        c = tuple([x, y])
        for d in [UP, LEFT]:
            h[c, d] = max(h[addcoord(c, d), d], g[c])


for y in reversed(range(0, Y)):
    for x in reversed(range(0, X)):
        c = tuple([x, y])
        for d in [DOWN, RIGHT]:
            h[c, d] = max(h[addcoord(c, d), d], g[c])


for y in range(0, Y):
    for x in range(0, X):
        c = tuple([x, y])
        v = False
        for d in dirs:
            v = v or (h[addcoord(c, d), d] < g[c])
        if v:
            visible.add(c)

print(len(visible))

def get_sd(c, d):
    m = g[c]
    sd = 0
    c = addcoord(c, d)
    while c in g:
        sd += 1
        if g[c] >= m:
            break
        c = addcoord(c, d)
    return sd

max_ss = 0
for y in range(0, Y):
    for x in range(0, X):
        c = tuple([x, y])
        sd = { d: get_sd(c, d) for d in dirs }
        ss = sd[UP] * sd[DOWN] * sd[LEFT] * sd[RIGHT]
        max_ss = max(max_ss, ss)

print(max_ss)

    
