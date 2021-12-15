#!/usr/bin/python3

import sys

m = []

r = 0
c = 0
for l in sys.stdin:
    m.append([int(i) for i in l.strip()])

rl = 0

def nbrs(x, y, l):
    out = []
    if x > 0:
        out += [(-1, 0)]
    if x < len(l) -1:
        out += [(1, 0)]
    if y > 0:
        out += [(0, -1)]
    if y < len(l[0]) - 1:
        out += [(0, 1)]
    return out

l = m

bsm = {}
bsc = {}

for x in range(len(l)):
    for y in range(len(l[0])):
        v = l[x][y]
        low = True
        for (dx, dy) in nbrs(x, y, l):
            low = low and l[x + dx][y + dy] > v
        if low:
            rl += v + 1
            bsm[(x, y)] = (x, y)
            bsc[(x, y)] = 1

print(rl)

print(bsm)

def ns(x, y, l):
    return [(x + dx, y + dy) for (dx, dy) in nbrs(x, y, l)]

found = True
while found:
    found = False
    for x in range(len(l)):
        for y in range(len(l[0])):
            v = l[x][y]
            if v == 9:
                continue
            if (x, y) in bsm:
                continue
            bs = set([bsm[n] for n in ns(x, y, l) if n in bsm])
            if len(bs) == 0:
                continue
            if len(bs) > 1:
                print(f"hm? {bs}")
            print(f"neighbor of {bs}")
            b = list(bs)[0]
            
            low = True
            for (z, w) in ns(x, y, l):
                low = low and (l[z][w] >= v or (z, w) in bsm)
            if low:
                print(f"found!")
                bsm[(x, y)] = b
                bsc[b] += 1
                found = True

for x in range(len(l)):
    for y in range(len(l[0])):
        if (not (x, y) in bsm) and l[x][y] != 9:
            print(f"problem: {x},{y}")


btop = sorted(bsc.values())

print(btop)
print(btop[-1]*btop[-2]*btop[-3])



