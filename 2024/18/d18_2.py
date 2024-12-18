#!/usr/bin/python3

import sys
import re
from collections import defaultdict
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

X = 71
Y = 71
first = 1024

#X = 7
#Y = 7
#first = 12

g = defaultdict(None)

E = X - 1 + 1j*(Y - 1)


def gg(p):
    if 0 > int(p.real) or X <= int(p.real) or 0 > int(p.imag) or Y <= int(p.imag):
        return '#'
    elif p in g:
        return g[p]
    else:
        return '.'

d = defaultdict(None)
q = PriorityQueue()
dirs = [1+0j, -1+0j, 0+1j, 0-1j]

def reachable():
    q.put((0, str(0 + 0j)))

    while not q.empty():
        (dist, p) = q.get()
        p = complex(p)

        if p in d and d[p] <= dist:
            continue

        if gg(p) == '#':
            continue

        d[p] = dist

        if p == E:
            break

        for dr in dirs:
            q.put((dist + 1, str(p + dr)))

    return E in d

def fill(n):
    global g
    g = defaultdict(None)
    for l in ls[:n]:
        x, y = nums(l)
        g[x + 1j*y] = '#'

kg = 1023
kb = len(ls)

while kb - kg > 1:
    end = (kg + kb) // 2
    d = dict()
    q = PriorityQueue()
    fill(end)
    if reachable():
        kg = end
    else:
        kb = end

print(ls[kb - 1])




