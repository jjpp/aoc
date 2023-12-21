#!/usr/bin/python3

import sys
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)
sy = min([i for i in range(0, Y) if 'S' in ls[i]])
sx = ls[sy].index('S')

d = {}
q = PriorityQueue()

ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

q.put((0, (sx, sy)))

while not q.empty():
    (dist, (x, y)) = q.get()
    if x < 0 or x >= X or y < 0 or y >= Y:
        continue

    if ls[y][x] == '#':
        continue

    if (x, y, dist % 2) in d:
        continue

    d[x, y, dist % 2] = dist

    for d_ in ds:
        q.put((dist + 1, (x + d_[0], y + d_[1])))


steps = 64
print(sum([1 if d[(x, y, dist)] <= steps and dist % 2 == steps % 2 else 0 for (x, y, dist) in d]))

        
