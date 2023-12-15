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

b = {}

for c in l.split(','):
    if c[-1] == '-':
        lbl = c[:-1]
        v = None
    else:
        (lbl, v) = c.split('=')

    box = h(lbl)

    if box not in b:
        b[box] = {}

    if v == None:
        if lbl in b[box]:
            del b[box][lbl]
    else:
        b[box][lbl] = int(v)

s = 0
for box in b:
    slot = 1
    # dicts in python3 remember the order of adding the keys
    for lens in b[box]:
        s += (box + 1) * slot * b[box][lens]
        slot += 1

print(s)


