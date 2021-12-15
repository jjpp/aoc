#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

pts = {}

for l in ls:
    p = l.split(' -> ')
    (x0, y0) = [int(n) for n in p[0].split(',')]
    (x1, y1) = [int(n) for n in p[1].split(',')]

    if not (x0 == x1 or y0 == y1):
        continue
    
    for x in range(min(x0, x1), max(x0, x1)+1):
        for y in range(min(y0, y1), max(y0, y1) + 1):
            pts[x, y] = pts.get((x, y), 0) + 1


print(len([x for x in pts.values() if x > 1]))



