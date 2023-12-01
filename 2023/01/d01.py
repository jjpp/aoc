#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def value(l):
    nrs = [ k for k in l if k >= '0' and k <= '9' ]
    return int(nrs[0] + nrs[-1])

print(sum([value(l) for l in ls]))

