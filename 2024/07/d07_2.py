#!/usr/bin/python3

# part 2

import sys

ls = [l.strip() for l in sys.stdin]

def can_be_true(t, d):
    if len(d) == 1:
        return t == d[0]

    a, b, rest = d[0], d[1], d[2:]

    return     can_be_true(t, [a + b, *rest]) \
            or can_be_true(t, [a * b, *rest]) \
            or can_be_true(t, [int(str(a) + str(b)), *rest])

s = 0
for l in ls:
    d = l.split()
    t = int(d.pop(0)[0:-1])
    d = [int(d_) for d_ in d]
    if can_be_true(t, d):
        s += t

print(s)


