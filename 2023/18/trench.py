#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ds = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
}

t = {}

x = 1
y = 1

minx = maxx = miny = maxy = 1

t[1, 1] = 1

for l in ls:
    (d, l, c) = l.split()
    l = int(l)

    for i in range(0, l):
        x += ds[d][0]
        y += ds[d][1]
        t[x, y] = 1
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)

#for y in range(miny, maxy + 1):
#    print("".join(['#' if (x, y) in t else '.' for x in range(minx, maxx + 1)]))

def fill(x, y, v):
    q = [(x, y)]
    while len(q) > 0:
        (x, y) = q.pop()
        if x < minx or x > maxx or y < miny or y > maxy:
            continue
        if (x, y) in t:
            continue

        t[x, y] = v
        for d in ds:
            q.append((x + ds[d][0], y + ds[d][1]))

for y in range(miny, maxy +1):
    fill(minx, y, 0)
    fill(maxx, y, 0)

for x in range(minx, maxx + 1):
    fill(x, miny, 0)
    fill(x, maxy, 0)

for y in range(miny, maxy +1):
    for x in range(minx, maxx + 1):
        if (x, y) not in t:
            t[x, y] = 1

#for y in range(miny, maxy + 1):
#    print("".join([str(t[x,y]) if (x, y) in t else '.' for x in range(minx, maxx + 1)]))

print(sum(t.values()))

