#!/usr/bin/python3

import sys

ls = [l.strip().split(' ') for l in sys.stdin]

xs = sorted([int(l[0]) for l in ls])
ys = sorted([int(l[3]) for l in ls])

print(sum([x * ys.count(x) for x in xs]))



