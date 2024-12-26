#!/usr/bin/python3

# part 1

import sys
import re

ls = [l.strip() for l in sys.stdin]

towels = list(sorted(ls[0].split(', ')))

p = dict()

def possible(l):
    if l in towels:
        return 1
    if l in p:
        return p[l]
    for t in towels:
        if l[0:len(t)] == t and possible(l[len(t):]) == 1:
            p[l] = 1
            return 1
    p[l] = 0
    return 0

print(sum([possible(l) for l in ls[2:]]))


