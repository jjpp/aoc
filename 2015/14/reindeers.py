#!/usr/bin/python3

import sys

rd = {}

for line in sys.stdin:
    [name, _, _, fly, _, _, duration, _, _, _, _, _, _, rest, _] = line.strip().split(' ')
    rd[name] = [int(fly), int(duration), int(rest), int(duration) + int(rest)]

T = 2503

pts = {}
maxp = 0

for t in range(1, T + 1):
    maxd = 0
    ds = {}
    for k in rd.keys():
        r = rd[k]
        print(r)
        d = int(t / r[3]) * r[0] * r[1] + (min(t % r[3], r[1]) * r[0])
        print(k, d)
        maxd = max(d, maxd)
        ds[k] = d

    for k in rd.keys():
        if ds[k] == maxd:
            pts[k] = pts.get(k, 0) + 1
            maxp = max(maxp, pts[k])

print(maxp)
