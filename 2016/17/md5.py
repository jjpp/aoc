#!/usr/bin/python3

import sys
import hashlib

pref = "edjrjqaa"

ps = [("", 0, 0, 0)]

dirs = "UDLR"
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while len(ps) > 0:
    (path, x, y, steps) = ps.pop(0)

    if x == 3 and y == 3:
        print(steps, path, len(ps))
        continue

    md5 = hashlib.md5((pref + path).encode('ascii')).hexdigest()
    for i in range(0, len(dirs)):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if x_ not in range(0, 4) or y_ not in range(0, 4):
            continue
        if md5[i] not in "bcdef":
            continue
        ps.append((path + dirs[i], x_, y_, steps + 1))

