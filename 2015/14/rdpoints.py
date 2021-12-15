#!/usr/bin/python3

import sys

rd = {}

for line in sys.stdin:
    [name, _, _, fly, _, _, duration, _, _, _, _, _, _, rest, _] = line.strip().split(' ')
    rd[name] = [int(fly), int(duration), int(rest), int(duration) + int(rest)]

T = 2503

maxd = 0
for k in rd.keys():
    r = rd[k]
    print(r)
    d = int(T / r[3]) * r[0] * r[1] + (min(T % r[3], r[1]) * r[0])
    print(k, d)
    maxd = max(d, maxd)

print(maxd)


