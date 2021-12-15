#!/usr/bin/env python3

import sys

x = 0
y = 0
aim = 0

for l in sys.stdin:
    (cmd, a) = l.strip().split(' ')
    a = int(a)

    if cmd == "forward":
        x += a
        y += (aim * a)
    elif cmd == "up":
        aim -= a
    elif cmd == "down":
        aim += a

print(x, y, x*y)


