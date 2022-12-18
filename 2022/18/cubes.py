#!/usr/bin/python3

import sys
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

cs = {}
mx = 0
mn = 1000

for l in ls:
    ns = [int(n) for n in l.split(',')]
    cs[tuple(ns)] = 1
    mx = max(mx, max(ns))
    mn = min(mn, min(ns))


os = 0

sides = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

for k in cs:
    (x, y, z) = k

    for d in sides:
        (dx, dy, dz) = d
        if (x + dx, y + dy, z + dz) not in cs:
            os += 1

print(os)

mn -= 1
mx += 1

   
dists = {}
q = PriorityQueue()

dists[(mn, mn, mn)] = 0
q.put((0, (mn, mn, mn)))

while not q.empty():
    (dist, p) = q.get()
    (x, y, z) = p
    for d in sides:
        (dx, dy, dz) = d
        if x + dx < mn or x + dx > mx or y + dy < mn or y + dy > mx or z + dz < mn or z + dz > mx:
            continue
        if (x + dx, y + dy, z + dz) in cs:
            continue
        if (x + dx, y + dy, z + dz) not in dists or dists[(x + dx, y + dy, z + dz)] > dists[(x, y, z)] + 1:
            dists[(x + dx, y + dy, z + dz)] = dists[(x, y, z)] + 1
            q.put((dists[(x + dx, y + dy, z + dz)], (x + dx, y + dy, z + dz)))


es = 0
for x in range(mn + 1, mx):
    for y in range(mn + 1, mx):
        for z in range(mn + 1, mx):
            if (x, y, z) in dists:
                continue
            for d in sides:
                (dx, dy, dz) = d
                if (x + dx, y + dy, z + dz) in dists:
                    es += 1

print(es)

