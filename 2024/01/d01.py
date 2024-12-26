#!/usr/bin/python3

# part 1

import sys

ls = [l.strip().split(' ') for l in sys.stdin]

xs = sorted([int(l[0]) for l in ls])
ys = sorted([int(l[3]) for l in ls])

print(sum([abs(z[0] - z[1]) for z in zip(xs, ys)]))


