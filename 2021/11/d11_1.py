#!/usr/bin/python3

import sys

m = {}

for y in range(10):
    l = sys.stdin.readline().strip()
    for (x, c) in enumerate(l):
        m[x, y] = int(c)

def nbrs(x, y): 
    out = []
    for dx in [-1, 0, 1]:
        if x + dx >= 0 and x + dx < 10:
            for dy in [-1, 0, 1]:
                if y + dy >= 0 and y + dy < 10:
                    if dx != 0 or dy != 0:
                        out += [(x + dx, y + dy)]
    return out

def step(m):
    f = 0
    mo = {}

    for y in range(10):
        for x in range(10):
            mo[x, y] = mo.get((x, y), 0) + m[x, y] + 1

    while (sum([1 for v in mo.values() if v > 9]) > 0):
        for y in range(10):
            for x in range(10):
                if mo[x, y] > 9:
                    f += 1
                    mo[x, y] = 0
                    for (w, z) in nbrs(x, y):
                        if (w, z) in mo and mo[w, z] > 0:
                            mo[w, z] += 1

    return (f, mo)

def p(m):
    for y in range(10):
        l = "".join([str(m[x, y]) if m[x, y] > 0 else "_" for x in range(10)])
        print(l)


f = 0
for s in range(100):
    (fn, mn) = step(m)
    print(fn)
    p(mn)
    f += fn
    m = mn

print(f)

s = 100
while sum([1 for v in m.values() if v == 0]) < 100:
    s += 1
    (fn, m) = step(m)

print(s)

