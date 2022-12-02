#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

w = {
        (0, 0): 3,
        (0, 1): 6,
        (0, 2): 0,
        (1, 0): 0,
        (1, 1): 3,
        (1, 2): 6,
        (2, 0): 6,
        (2, 1): 0,
        (2, 2): 3
}

st = {
        (0, 0): 2,
        (0, 1): 0,
        (0, 2): 1,
        (1, 0): 0,
        (1, 1): 1,
        (1, 2): 2,
        (2, 0): 1,
        (2, 1): 2,
        (2, 2): 0
}

s = 0

for g in ls:
    (e, y) = g.split(' ')
    e_ = ord(e) - ord('A')
    y_ = ord(y) - ord('X')
    y_ = st[(e_, y_)]
    s += w[(e_, y_)] + y_ + 1

print(s)
