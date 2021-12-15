#!/usr/bin/python3

import sys

l = {}

def set_lights(v, coord):
    [a, zz, b] = coord.split(' ')
    [x0, y0] = [int(z) for z in a.split(',')]
    [x1, y1] = [int(z) for z in b.split(',')]

    for x in range(min(x0, x1), max(x0, x1) + 1):
        for y in range(min(y0, y1), max(y0, y1) + 1):
            l[x, y] = max(v + l.get((x, y), 0), 0)

for x in range(0, 1000):
    for y in range(0, 1000):
        l[x, y] = 0

for ln in sys.stdin:
    if ln.startswith('turn on '):
        set_lights(1, ln[8:])
    elif ln.startswith('turn off '):
        set_lights(-1, ln[9:])
    elif ln.startswith('toggle '):
        set_lights(2, ln[7:])

c = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        c += l[x, y]

print(c)

