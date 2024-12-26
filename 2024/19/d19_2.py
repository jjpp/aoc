#!/usr/bin/python3

# part 2

import sys
import re

ls = [l.strip() for l in sys.stdin]

towels = list(sorted(ls[0].split(', ')))

p = dict()

p[""] = 0

def possible(l):
    if l in p:
        return p[l]

    p[l] = 1 if l in towels else 0

    for t in towels:
        if l[0:len(t)] == t:
            p[l] += possible(l[len(t):])

    return p[l]

print(sum([possible(l) for l in ls[2:]]))


