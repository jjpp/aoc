#!/usr/bin/python3

import sys

lns = [l.strip() for l in sys.stdin]

grid = {}


maxx = maxy = 0
first = True

for l in lns:
    if l == "":
        ...
    elif l.startswith("fold along x="):
        f = int(l[13:])
        wrap = []
        for (x, y) in grid.keys():
            if x > f:
                wrap.append((x, y))
        for (x, y) in wrap:
            grid[2 * f - x, y] = grid[x, y]
            del grid[x, y]
        maxx = f
        if first:
            print(len(grid))
            first = False
    elif l.startswith("fold along y="):
        f = int(l[13:])
        wrap = []
        for (x, y) in grid.keys():
            if y > f:
                wrap.append((x, y))
        for (x, y) in wrap:
            grid[x, 2*f - y] = grid[x, y]
            del grid[x, y]
        maxy =f
        if first:
            print(len(grid))
            first = False
    else:
        (x, y) = [int(z) for z in l.split(',')]
        grid[x, y] = True



for y in range(maxy):
    print("".join(["#" if (x, y) in grid else "." for x in range(maxx)]))


