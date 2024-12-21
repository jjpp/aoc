#!/usr/bin/python3

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
no_cheat = 0 + 0j

def g(p, pp, cheat):
    if not ((0 <= int(p.real) < X) and (0 <= int(p.imag) < Y)):
        return '#'
    if p == cheat[0] or (p == cheat[1] and pp == cheat[0] and ls[int(p.imag)][int(p.real)] != '#'):
        return '.'
    else:
        return ls[int(p.imag)][int(p.real)]

m = {}
rm = {}
for x in range(X):
    for y in range(Y):
        c = x + 1j*y
        s = 1000 * x + y
        m[s] = c
        rm[c] = s

def check_and_add(p, dist, d, q, pp, c1, c2):
    if g(p, pp, (c1, c2)) != '#' and ((p, c1, c2) not in d or d[p, c1, c2] > dist):
        q.put((dist, rm[c1], rm[c2], rm[p]))


d = defaultdict(None)
bd = 0
def shortest():
    q = PriorityQueue()
    q.put((0, rm[no_cheat], rm[no_cheat], rm[S]))
    bestdist = None
    global bd
    while not q.empty():
        (dist, c1, c2, p) = q.get()
        p = m[p]
        c1 = m[c1]
        c2 = m[c2]

        if not ((0 < int(p.real) < X) and (0 < int(p.imag) < Y)):
            continue

        if (p, c1, c2) in d and d[p, c1, c2] <= dist:
            continue

        if (p, no_cheat, no_cheat) in d and d[p, no_cheat, no_cheat] <= dist:
            continue

        if (E, c1, c2) in d:
            continue

        d[p, c1, c2] = dist

        if p == E:
            print(p, c1, c2, dist, q.qsize(), len(d.keys()))
            if c1 == no_cheat and c2 == no_cheat:
                return

        if bd < dist:
            bd = dist
            print(p, c1, c2, dist, q.qsize(), len(d.keys()), "distjump")

        if (c1 == no_cheat and c2 == no_cheat) or (c1 != no_cheat and c2 != no_cheat):
            for dr in ds:
              check_and_add(p + dr, dist + 1, d, q, p, c1, c2)

        if c1 == no_cheat:
          for dr in ds:
            check_and_add(p + dr, dist + 1, d, q, p, p + dr, c2)

        if c1 == p and c2 == no_cheat:
          for dr in ds:
            check_and_add(p + dr, dist + 1, d, q, p, c1, p + dr)
        

print(X, Y)
shortest()

#cc = [d[E, no_cheat, no_cheat] - d[p] for p in d if p[0] == E and d[E, no_cheat, no_cheat] - d[p] > 0]
#for l in sorted(list(set(cc))):
#    print(l, cc.count(l), [p for p in d if p[0] == E and d[E, no_cheat, no_cheat] - d[p] == l])
#print(len(cc))


print(sum([1 for p in d if p[0] == E and d[E, no_cheat, no_cheat] - d[p] > 99]))

