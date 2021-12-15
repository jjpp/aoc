#!/usr/bin/env python3

import sys

x = 0
y = 0

for l in sys.stdin:
    (cmd, a) = l.strip().split(' ')
    a = int(a)

    if cmd == "forward":
        x += a
    elif cmd == "up":
        y -= a
    elif cmd == "down":
        y += a

print(x, y, x*y)


