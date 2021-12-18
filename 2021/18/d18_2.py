#!/usr/bin/python3

import sys
from copy import deepcopy

lns = [eval(l.strip()) for l in sys.stdin]

def at(n, _p):
    p = deepcopy(_p)
    #print(f"at({n}, {p})")
    while len(p) > 0:
        if isinstance(n, list):
            n = n[p[0]]
            p.pop(0)
        else:
            return None
    #print(f"returning '{n}'")
    return n

def leftof(n, _p):
    p = deepcopy(_p)
    while len(p) > 0 and p[-1] == 0:
        p = p[0:-1]
    if len(p) == 0:
        return None
    p[-1] = 0
    while isinstance(at(n, p), list):
        p.append(1)

    return p

def rightof(n, _p):
    p = deepcopy(_p)
    while len(p) > 0 and p[-1] == 1:
        p = p[0:-1]
    if len(p) == 0:
        return None
    p[-1] = 1
    while isinstance(at(n, p), list):
        p.append(0)

    return p

def explode(n, p):
    pair = at(n, p)
    #print(f"explode({n}, {p}) -- {pair}")

    left = leftof(n, p) 
    right = rightof(n, p)

    if left != None:
        #print(f"left = {left}")
        at(n, left[0:-1])[left[-1]] += pair[0]
    if right != None:
        #print(f"right = {right}, parent = {right[0:-1]}")
        at(n, right[0:-1])[right[-1]] += pair[1]

    #print(f"in {at(n, p[0:-1])} replacing {p[-1]}")

    at(n, p[0:-1])[p[-1]] = 0

def split(n, p):
    num = at(n, p)
    #print(f"split({n}, {p}) -- {num}")
    l = num // 2
    r = num - l
    at(n, p[0:-1])[p[-1]] = [l, r]

def rec_explode(n, p):
    x = at(n, p)
    if x == None:
        return False

    if len(p) > 3 and isinstance(x, list) and isinstance(x[0], int) and isinstance(x[1], int):
        explode(n, p)
        return True

    return rec_explode(n, p + [0]) or rec_explode(n, p + [1])

def rec_split(n, p):
    x = at(n, p)
    if x == None:
        return False

    if isinstance(x, int) and x > 9:
        split(n, p)
        return True

    return rec_split(n, p + [0]) or rec_split(n, p + [1])

def reduce(n):
    while rec_explode(n, []) or rec_split(n, []):
        ...
    return n

def mag(n):
    if isinstance(n, list):
        return 3* mag(n[0]) + 2*mag(n[1])
    return n


mm = 0
for (i, a) in enumerate(lns):
    for (j, b) in enumerate(lns):
        if (i == j):
            continue
        s = reduce([deepcopy(a), deepcopy(b)])
        mm = max(mm, mag(s))
        #print(f"{a} + {b} = {s} ({mag(s)})")

print(mm)

