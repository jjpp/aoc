#!/usr/bin/python3

import sys
from collections import Counter

ls = [l.strip().split() for l in sys.stdin]

def type(a):
    c = Counter(a)
    mc = c.most_common()
    if mc[0][1] == 5:
        return 1
    if mc[0][1] == 4:
        return 2
    if mc[0][1] == 3:
        if mc[1][1] == 2:
            return 3
        else:
            return 4
    if mc[0][1] == 2:
        if mc[1][1] == 2:
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

