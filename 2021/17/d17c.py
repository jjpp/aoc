#!/usr/bin/python3

import sys
import math

lns = [l.strip() for l in sys.stdin]

ls = lns[0].split(' ')
xs = [int(x) for x in ls[2].strip(',').split('=')[1].split('..')]
ys = [int(y) for y in ls[3].split('=')[1].split('..')]

out = 0
speeds = {}
c = 0

# x speed should be at least 1 and at most at the right edge of target area
for x in range(1, xs[1] + 1):
    maxx = x * (x + 1) / 2
    if maxx < xs[0]:
        continue

    minxt = max(int(xs[0] / x), 1)

    # y_target: where y should end up
    for yt in range(ys[0], ys[1] + 1):
        for t in range(minxt, -2*yt + 1):
            c += 1
            if not (2 * yt) % t == 0:
                continue
            drag = t * (t-1) / 2
            _x = maxx if t > x else t*x - drag
            if not xs[0] <= _x <= xs[1]:
                continue
            y = yt / t + (t - 1) / 2

            if y < ys[0]:
                break

            # must be an integer
            if y % 1:
                continue
            y = int(y)

            _y = y*t - drag
            if not ys[0] <= _y <= ys[1]:
                continue

            m = round((_y * (_y + 1) + 0.5) / 2)

            out = max(out, m)
            speeds[x, y] = m


        # print(t, x, y, c, out)

print(out)
print(len(speeds))
print(c)
