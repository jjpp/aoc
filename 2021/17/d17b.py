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

for x in range(1, xs[1] + 1):
    maxx = x * (x + 1) / 2
    if maxx < xs[0]:
        continue

    for t in range(1, 1000):
        drag = t * (t-1) / 2
        _x = maxx if t > x else t*x - drag
        if not (xs[0] <= _x <= xs[1]):
            continue

        miny = int(ys[0] / t + (t - 1) / 2)
        maxy = int((ys[1] + 1) / t + (t) / 2)

        if ((miny - 1) * t - drag) > ys[1] or ((maxy + 1) * t - drag) < ys[0]:
            continue

#        print(x, [miny, maxy], [(miny - 1) * t - drag, (maxy + 1) * t - drag], t)


        for y in range(miny - 1, maxy + 1):
            _y = y*t - drag
            if not (ys[0] <= _y <= ys[1]):
                continue

            c = check(x, y, t)
            if not c == None:
                speeds[x, y] = t
                if out == None or c > out:
                    out = c

        # print(t, x, y, c, out)

print(out)
print(len(speeds))
