#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def value(l):
    c = l.split()
    #i = int(c[1])
    bar = c.index('|')
    winning = c[2:bar]
    yours = c[bar:]
    points = [w for w in winning if w in yours]
    return int(2**(len(points) - 1))

print(sum([value(l) for l in ls]))

