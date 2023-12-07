#!/usr/bin/python3

import sys
from collections import Counter

ls = [l.strip().split() for l in sys.stdin]

def type(a):
    c = Counter(a)
    best = c.most_common()[0][1]

    if best == 5:
        return 1

    second_best = c.most_common()[1][1]

    if best == 4:
        return 2

    if best == 3:
        if second_best == 2:
            return 3
        else:
            return 4

    if best == 2:
        if second_best == 2:
            return 5
        else:
            return 6

    return 7

ranks = "23456789TJQKA"

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

