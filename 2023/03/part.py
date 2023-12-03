#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

adj = {}

max_y = len(ls)
max_x = len(ls[0])

partnum = 0

sym = False
num = ""

for y in range(0, max_y):
    for x in range(0, max_x):
        for d in range(0, len(dy)):
            x_ = x + dx[d]
            y_ = y + dy[d]
            if y_ not in range(0, max_y) or x_ not in range(0, max_x):
                continue
            if ls[y_][x_] not in '01234567890.':
                adj[x, y] = True

for y in range(0, max_y):
    sym = False
    num = ""
    for x in range(0, max_x):
        if ls[y][x] in '01234567890':
            num += ls[y][x]
            sym = sym or (x, y) in adj
        else:
            if sym and num != "":
                partnum += int(num)
            sym = False
            num = ""
    if sym and num != "":
        partnum += int(num)
    sym = False
    num = ""

print(partnum)

