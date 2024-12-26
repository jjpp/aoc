#!/usr/bin/python3

# part 1

import sys
import re

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = ls.index("")
cmds = "".join(ls[Y+1:])

for y in range(Y):
    if "@" in ls[y]:
        p = ls[y].index("@") + 1j*y

ds = {
        '<': -1,
        '>': 1,
        '^': -1j,
        'v': 1j
}

for y in range(Y):
    ls[y] = list(ls[y])

def g(p):
    return ls[int(p.imag)][int(p.real)]

def setg(p, v):
    ls[int(p.imag)][int(p.real)] = v

def printg():
    for y in range(Y):
        print("".join(ls[y]))

setg(p, '.')

def step(p, d):
    np = p + ds[d]
    if g(np) == '.':
        p = np
        # print("free step")
    elif g(np) == '#':
        p = p
        # print("wall")
    elif g(np) == 'O':
        lp = np
        # print("block")
        while g(lp) == 'O':
            lp = lp + ds[d]
        # print("behind it: ", lp, g(lp))
        if g(lp) == '.':
            setg(lp, 'O')
            setg(np, '.')
            p = np
    return p

for c in cmds:
    p = step(p, c)
    #printg()
    #print(p, c)
    #print()

s = 0
for y in range(Y):
    for x in range(X):
        if ls[y][x] == 'O':
            s += 100*y + x

print(s)

