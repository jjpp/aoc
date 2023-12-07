#!/usr/bin/python3

import sys
from collections import Counter

ls = [l.strip().split() for l in sys.stdin]


def type(a):
    c = Counter(a)
    mc = c.most_common()

    j = c.get('J', 0)

    if j == 5:
        return 1

    best = (mc[1][1] if mc[0][0] == 'J' else mc[0][1]) + j
    sb = (mc[2][1] if best != 5 and mc[1][0] == 'J' else mc[1][1])

    if best == 5:
        return 1
    if best == 4:
        return 2
    if best == 3:
        if sb == 2:
            return 3
        else:
            return 4
    if best == 2:
        if sb == 2:
            return 5
        else:
            return 6
    return 7

ranks = "J23456789TQKA"

def key(a):
    r = 10 - type(a)
    for i in range(0, 5):
        r = (r * len(ranks)) + ranks.index(a[i])
    return r

o = list(sorted(ls, key = lambda p: key(p[0])))

s = 0
for i in range(0, len(o)):
    s += (i+1) * int(o[i][1])

print(s)

