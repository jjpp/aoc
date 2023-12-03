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

gears = {}
gcount = {}

for y in range(0, max_y):
    num = ""
    for x in range(0, max_x):
        for d in range(0, len(dy)):
            x_ = x + dx[d]
            y_ = y + dy[d]
            if y_ not in range(0, max_y) or x_ not in range(0, max_x):
                continue
            if ls[y_][x_] == '*':
                if (x, y) in adj:
                    adj[x, y].add((x_, y_))
                else:
                    adj[x, y] = set([(x_, y_)])

for y in range(0, max_y):
    g = set()
    num = ""
    for x in range(0, max_x):
        if ls[y][x] in '01234567890':
            num += ls[y][x]
            if (x, y) in adj:
                g |= adj[x, y]
        else:
            if len(g) > 0 and num != "":
                for sym in g:
                    if not sym in gears:
                        gears[sym] = int(num)
                        gcount[sym] = 1
                    else:
                        gears[sym] *= int(num)
                        gcount[sym] += 1
            num = ""
            g = set()
    if len(g) > 0 and num != "":
        for sym in g:
            if not sym in gears:
                gears[sym] = int(num)
                gcount[sym] = 1
            else:
                gears[sym] *= int(num)
                gcount[sym] += 1
    num = ""
    g = set()

print(sum([gears[x] if gcount[x] == 2 else 0 for x in gears if gcount[x] == 2]))

