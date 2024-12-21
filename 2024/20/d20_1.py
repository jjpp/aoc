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

cheat = (0 + 0j, 0 + 0j)
def g(p, pp):
    if p == cheat[0] or (p == cheat[1] and pp == cheat[0]):
        return '.'
    else:
        return ls[int(p.imag)][int(p.real)]

def check_and_add(p, dist, d, q, pp):
    if g(p, pp) != '#' and ((p) not in d or d[p] > dist):
        q.put((dist, str(p)))


def shortest():
    d = defaultdict(None)
    q = PriorityQueue()
    q.put((0, str(S)))
    bestdist = None
    while not q.empty():
        (dist, p) = q.get()
        p = complex(p)
        if (p) in d and d[p] <= dist:
            continue

        d[p] = dist

        if p == E and bestdist == None:
            return dist
            bestdist = dist

        for dr in ds:
          check_and_add(p + dr, dist + 1, d, q, p)

    return None

print(X, Y)
best = shortest()
print(best)

cc = 0
for y in range(1, Y - 1):
    for x in range(1, X - 1):
        p = x + 1j * y
        print(y, p)        
        for d_ in ds:
            p2 = p + d_
            if 0 < int(p2.real) < (X-1) and 0 < int(p2.imag) < (Y - 1):
                cheat = (p, p2)
                pl = shortest()
                if best - pl >= 100:
                    cc += 1
                print(cheat, pl, cc)

print(cc)
