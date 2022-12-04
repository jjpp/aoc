#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


count = 0
for ps in ls:
    p1, p2 = ps.split(',')
    [p1f, p1l] = [int(x) for x in p1.split('-')]
    [p2f, p2l] = [int(x) for x in p2.split('-')]

    print(ps)
    print(p1f, p1l, p2f, p2l)


    if (p1f <= p2f <= p1l) or (p1f <= p2l <= p1l) or (p2f <= p1f <= p2l) or (p2f <= p1l <= p2f) or (p1f <= p2f and p1l >= p2l) or (p2f <= p1f and p2f >= p1f):

        count += 1

print(count)
