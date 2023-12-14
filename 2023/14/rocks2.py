#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)


def tilt(r):
    l = 0
    o = []
    for i in range(0, len(r)):
        if r[i] == '#':
            o.append('.' * (i - l))
            o.append('#')
            l = i + 1
        elif r[i] == 'O':
            o.append('O')
            l += 1

    o.append('.' * (len(r) - l))

    o = "".join(reversed(o))

    return o

def cycle(ls):
    for i in range(0, 4):
        ls = [tilt(r) for r in list(zip(*ls))]

    return ls

def weight(ls):
    s = 0
    for y in range(0, Y):
        s += (Y - y) * sum([1 if c == 'O' else 0 for c in ls[y]])
    return s

c = 1
first = None
seen = {}
w = {}
while True:
    ls = cycle(ls)
    full = "".join(ls)
    if full in seen:
        print("Cycle", c, seen[full])
        first = seen[full]
        break
    seen[full] = c
    w[c] = weight(ls)
    c += 1

step = (1000000000 - c) % (c - first) + first
print(w[step])
