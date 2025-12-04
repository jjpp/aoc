#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

Y = len(ls)
X = len(ls[0])

def count_rolls(x, y):
    c = 0
    for d_ in d:
        if 0 <= x+d_[0] < X and 0 <= y+d_[1] < Y and ls[y+d_[1]][x+d_[0]] == '@':
            c += 1
    return c

tc = 0
for y in range(0, Y):
    for x in range(0, X):
        if ls[y][x] == '@' and count_rolls(x, y) < 4:
            tc += 1

print(tc)
