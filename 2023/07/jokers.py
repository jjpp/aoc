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

    b = 1 if mc[0][0] == 'J' else 0
    sb = 2 if mc[0][1] != 5 and mc[1][0] == 'J' else 1

    if mc[b][1] + j == 5:
        return 1
    if mc[b][1] + j == 4:
        return 2
    if mc[b][1] + j == 3:
        if mc[sb][1] == 2:
            return 3
        else:
            return 4
    if mc[b][1] + j == 2:
        if mc[sb][1] == 2:
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

