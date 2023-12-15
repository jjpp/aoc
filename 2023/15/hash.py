#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

l = "".join(ls)

def h(s):
    h = 0
    for x in s:
        h += ord(x)
        h *= 17
        h %= 256
    return h

print(sum([h(x) for x in l.split(',')]))

