#!/usr/bin/python3

# part 1 & 2

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

d = defaultdict(None)
q = PriorityQueue()
q.put((0, 1+0j, S))

ds = [1+0j, -1+0j, 0+1j, 0-1j]

def g(p):
    return ls[int(p.imag)][int(p.real)]

def check_and_add(p, dr, dist):
    if g(p) != '#' and ((p, dr) not in d or d[p, dr] > dist):
        q.put((dist, str(dr), str(p)))

bestdist = None
while not q.empty():
    (dist, dr, p) = q.get()
    dr = complex(dr)
    p = complex(p)
    if (p, dr) in d and d[p, dr] <= dist:
        continue

    d[p, dr] = dist

    if p == E and bestdist == None:
        print(dist)
        bestdist = dist

    check_and_add(p + dr, dr, dist + 1)
    check_and_add(p, dr * 1j, dist + 1000)
    check_and_add(p, dr * -1j, dist + 1000)

bests = set()
bests.add(E)
check = []
for dr in ds: 
    if (E, dr) in d and d[E, dr] == bestdist:
        check.append((E, dr, bestdist))

def caa2(p, dr, dist):
    if (p, dr) in d and d[p, dr] == dist:
        bests.add(p)
        check.append((p, dr, dist))

while len(check) > 0:
    (p, dr, dist) = check.pop()

    caa2(p - dr, dr, dist - 1)
    caa2(p, 1j * dr, dist - 1000)
    caa2(p, -1j * dr, dist - 1000)

print(len(bests))

