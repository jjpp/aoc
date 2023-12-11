#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

xs = set()
ys = set()

for j in range(0, Y):
    for i in range(0, X):
        if ls[j][i] == '#':
            xs.add(i)
            ys.add(j)

for x in reversed(sorted(list(set(range(0, X)) - xs))):
    for y in range(0, Y):
        ls[y] = ls[y][0:x] + '.' + ls[y][x:]

for y in reversed(sorted(list(set(range(0, Y)) - ys))):
    ls.insert(y, '.' * len(ls[0]))

X = len(ls[0])
Y = len(ls)

gs = []

for j in range(0, Y):
    for i in range(0, X):
        if ls[j][i] == '#':
            gs.append((i, j))

ds = []

for i in range(0, len(gs)):
    for j in range(i + 1, len(gs)):
        ds.append(abs(gs[i][0] - gs[j][0]) + abs(gs[i][1] - gs[j][1]))

print(sum(ds))

