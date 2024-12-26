#!/usr/bin/python3

# part 2

import sys
import re
from collections import defaultdict
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

ls = [list(l) for l in ls]
X = len(ls[0])
Y = len(ls)

for y in range(Y):
    if 'S' in ls[y]:
        S = y * 1j + ls[y].index('S')
    if 'E' in ls[y]:
        E = y * 1j + ls[y].index('E')


ds = [1+0j, -1+0j, 0+1j, 0-1j]

def in_g(p):
    return 0 < int(p.real) < (X - 1) and (0 < int(p.imag) < (Y - 1))
def g(p):
    if in_g(p):
        return ls[int(p.imag)][int(p.real)]
    else:
        return '#'

def check_and_add(p, dist, d, q):
    if g(p) != '#' and (p not in d or d[p] > dist):
        q.put((dist, str(p)))


bd = 0
def dists(S, E):
    d = defaultdict(lambda: 10*X*Y)
    q = PriorityQueue()
    q.put((0, str(S)))
    bestdist = None
    global bd
    while not q.empty():
        (dist, p) = q.get()
        p = complex(p)

        if p in d and d[p] <= dist:
            continue

        d[p] = dist

        if p == E:
            return d

        for dr in ds:
          check_and_add(p + dr, dist + 1, d, q)
        

s2e = dists(S, E)
e2s = dists(E, S)
nocheat = s2e[E]

cheats = set()

reachable = {}
reachable = { 0 + 0j: 0 }
for dist in range(20):
    ps = [ p for p in reachable if reachable[p] == dist]
    for p in ps: 
        for d in ds:
            q = p + d
            if q not in reachable or reachable[q] > dist + 1:
                reachable[q] = dist + 1

#print(len(reachable))

for y in range(Y):
    for x in range(X):
        start = x + 1j*y
        if g(start) != '#':
            for r in reachable:
                stop = start + r
                if not (in_g(start) and in_g(stop)):
                    continue

                if g(stop) != '#':
                    if e2s[start] + s2e[stop] + reachable[r] <= nocheat - 100:
                        cheats.add((start, stop))

print(len(cheats))

