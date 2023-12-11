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

gs = []

for j in range(0, Y):
    for i in range(0, X):
        if ls[j][i] == '#':
            gs.append((i, j))

ds = []

xs = set(range(0, X)) - xs
ys = set(range(0, Y)) - ys

for i in range(0, len(gs)):
    for j in range(i + 1, len(gs)):
        extra_x = len([x for x in xs if x > min(gs[i][0], gs[j][0]) and x < max(gs[i][0], gs[j][0])])
        extra_y = len([x for x in ys if x > min(gs[i][1], gs[j][1]) and x < max(gs[i][1], gs[j][1])])
        ds.append(abs(gs[i][0] - gs[j][0]) + abs(gs[i][1] - gs[j][1]) + 999999 * (extra_x + extra_y))

print(sum(ds))

