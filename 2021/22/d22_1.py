#!/usr/bin/python3

import sys

lns = [l.strip() for l in sys.stdin]

g = {}
cmds = []

for l in lns:
    (mode, coord) = l.split(' ')
    (xs, ys, zs) = [[int(x) for x in s.split('=')[1].split('..')] for s in coord.split(',')]

    cmds.append((mode, xs, ys, zs))

    for x in range(max(xs[0], -50), min(xs[1] + 1, 51)):
        for y in range(max(ys[0], -50), min(ys[1] + 1, 51)):
            for z in range(max(zs[0], -50), min(zs[1] + 1, 51)):
                g[x, y, z] = 1 if mode == 'on' else 0


print(sum(g.values()))
