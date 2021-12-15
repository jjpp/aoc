#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

pts = {}

for l in ls:
    p = l.split(' -> ')
    (x0, y0) = [int(n) for n in p[0].split(',')]
    (x1, y1) = [int(n) for n in p[1].split(',')]

    if not (x0 == x1 or y0 == y1 or (abs(x0 - x1) == abs(y0 - y1))):
        continue

    dx = 0 if x0 == x1 else (x1 - x0) / abs(x1 - x0)
    dy = 0 if y0 == y1 else (y1 - y0) / abs(y1 - y0)
    
    for d in range(0, max(abs(x0 - x1), abs(y0 - y1)) + 1):
        x = x0 + d*dx
        y = y0 + d*dy
        pts[x, y] = pts.get((x, y), 0) + 1


print(len([x for x in pts.values() if x > 1]))



