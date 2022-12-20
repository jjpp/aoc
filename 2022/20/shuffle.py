#!/usr/bin/python3

import sys

ls = [int(l.strip()) for l in sys.stdin]
order = list(range(len(ls)))

for p in range(len(ls)):
    i = order.index(p)
    x = ls[i]

    s = x // abs(x) if x != 0 else 0
    for _ in range(abs(x)):
        ls[i] = ls[(len(ls) + i + s) % len(ls)]
        order[i] = order[(len(ls) + i + s) % len(ls)]
        i = (len(ls) + i + s) % len(ls)
    ls[i] = x
    order[i] = p


z = ls.index(0)

print(ls[(z + 1000) % len(ls)] + ls[(z + 2000) % len(ls)] + ls[(z + 3000) % len(ls)])



