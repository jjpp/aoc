#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def can_be_true(t, d):
    print("cbd(", t, d, ")")

    if len(d) == 1:
        return t == d[0]

    rest = d[2:]

    return can_be_true(t, [d[0] + d[1], *rest]) or can_be_true(t, [d[0] * d[1], *rest])

s = 0
for l in ls:
    d = l.split()
    t = int(d.pop(0)[0:-1])
    d = [int(d_) for d_ in d]
    if can_be_true(t, d):
        s += t

print(s)


