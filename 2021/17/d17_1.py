#!/usr/bin/python3

import sys
import math

lns = [l.strip() for l in sys.stdin]

ls = lns[0].split(' ')
xs = [int(x) for x in ls[2].strip(',').split('=')[1].split('..')]
ys = [int(y) for y in ls[3].split('=')[1].split('..')]

print(xs, ys)

def check(dx, dy, t):
    x = 0
    y = 0
    maxy = 0
    for z in range(t):
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

    return None

out = None
speeds = {}

for t in range(1, 1000):
    drag = t * (t - 1) / 2
    miny = int(ys[0] / t + (t - 1) / 2)
    maxy = int((ys[1] + 1) / t + (t) / 2)


    for y in range(miny - 1, maxy + 1):
        for x in range(xs[1] + 1):
            c = check(x, y, t)
            if not c == None:
                speeds[x, y] = t
                if out == None or c > out:
                    out = c

            # print(t, x, y, c, out)

print(out)
print(len(speeds))
#for (x, y) in speeds.keys():
#    print(f"{x},{y}")
#
