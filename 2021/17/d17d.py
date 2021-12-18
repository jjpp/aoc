#!/usr/bin/python3

import sys
import math

lns = [l.strip() for l in sys.stdin]

ls = lns[0].split(' ')
xs = [int(x) for x in ls[2].strip(',').split('=')[1].split('..')]
ys = [int(y) for y in ls[3].split('=')[1].split('..')]

def check(dx, dy):
    x = 0
    y = 0
    maxy = 0
    while True:
        if (dx > 0):
            x += dx
            dx -= 1
        y += dy
        maxy = max(maxy, y)
        dy -= 1

        # print("  ", z, x, y)
        if x > xs[1]:
            return None
        if y < ys[0] and dy < 0:
            return None

        if (xs[0] <= x <= xs[1]) and (ys[0] <= y <= ys[1]):
            return maxy

out = None
speeds = set()
count = 0

for x in range(1, max(xs)+1):
    for y in range(ys[0], -ys[0] + 1):
        count += 1
        c = check(x, y)
        if not c == None:
            speeds.add((x, y))
            if out == None or c > out:
                out = c

        # print(t, x, y, c, out)

print(out)
print(len(speeds))
print(count)
