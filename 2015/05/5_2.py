#!/usr/bin/python3

import sys

nice = 0

for w in sys.stdin:
    pc = 0
    dc = 0
    ps = {}
    for p in range(1, len(w) - 1):
        pair = w[p - 1] + w[p]
        if pair in ps and ps[pair] + 1 < p:
            pc += 1
        elif not pair in ps:
            ps[pair] = p 
        if p > 1 and w[p - 2] == w[p]:
            dc += 1

    print(pc, dc)
    if pc > 0 and dc > 0:
        nice += 1


print(nice)

