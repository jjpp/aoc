#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

Y = len(ls)
X = len(ls[0])

for i in range(0, Y):
    ls[i] = list(ls[i])

def count_rolls(x, y):
    c = 0
    for d_ in d:
        if 0 <= x+d_[0] < X and 0 <= y+d_[1] < Y and ls[y+d_[1]][x+d_[0]] == '@':
            c += 1
    return c


def removable():
    out = []
    for y in range(0, Y):
        for x in range(0, X):
            if ls[y][x] == '@' and count_rolls(x, y) < 4:
                out.append( (x, y) )
    return out

tc = 0

while True:
    r = removable()
    if len(r) == 0:
        break

    tc += len(r)

    for r_ in r:
        ls[r_[1]][r_[0]] = 'x'


print(tc)
