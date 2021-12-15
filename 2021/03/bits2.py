#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def keep(ls, reverse = False):
    pos = 0
    while len(ls) > 1:
        n = sum([int(l[pos:pos+1]) for l in ls])
        m = 1 if (n*2 >= len(ls)) else 0
        m = 1 - m if reverse else m
        print(pos, ls, n, len(ls), m)
        ls = [l for l in ls if int(l[pos:pos+1]) == m]
        pos += 1

    print(ls)

    return int(ls[0], 2)

o = keep(ls, False)
c = keep(ls, True)

print(o, c, o*c)

