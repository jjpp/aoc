#!/usr/bin/python3

import sys

ls = [l.strip().split(' ') for l in sys.stdin]

xs = sorted([int(l[0]) for l in ls])
ys = sorted([int(l[3]) for l in ls])

zs = {}

for i in ys:
    if i in zs:
        zs[i] += 1
    else:
        zs[i] = 1

print(sum([x * zs.get(x, 0) for x in xs]))



