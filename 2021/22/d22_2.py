#!/usr/bin/python3

import sys
import tqdm

lns = [l.strip() for l in sys.stdin]

g = {}
cmds = []

x_ = set()
y_ = set()
z_ = set()

for l in lns:
    (mode, coord) = l.split(' ')
    (xs, ys, zs) = [[int(x) for x in s.split('=')[1].split('..')] for s in coord.split(',')]

    cmds.append((mode, xs, ys, zs))
    x_.add(xs[0])
    x_.add(xs[1]+1)
    y_.add(ys[0])
    y_.add(ys[1]+1)
    z_.add(zs[0])
    z_.add(zs[1]+1)

xl = { x[0]: x[1] - x[0] for x in zip(sorted(x_), sorted(x_)[1:]) }
yl = { y[0]: y[1] - y[0] for y in zip(sorted(y_), sorted(y_)[1:]) }
zl = { z[0]: z[1] - z[0] for z in zip(sorted(z_), sorted(z_)[1:]) }

print(len(x_) * len(y_) * len(z_) * len(cmds))

for c in tqdm.tqdm(cmds):
    for x in x_:
        if c[1][0] <= x <= c[1][1]:
            for y in y_:
                if c[2][0] <= y <= c[2][1]:
                    for z in z_:
                        if c[3][0] <= z <= c[3][1]:
                            g[x, y, z] = xl[x] * yl[y] * zl[z] if c[0] == 'on' else 0


print(sum(g.values()))

# 240438136260
# 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 420/420 [13:38<00:00,  1.95s/it]
# 1233304599156793

