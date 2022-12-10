#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


ss = [0]
x = 1
xs = []
cycle = 1

while len(ls) > 0:
    cmd = ls.pop(0)
    if cmd == 'noop':
        ss.append(x * cycle)
        xs.append(x)
        cycle += 1
    else:
        diff = int(cmd[5:])
        ss.append(x * cycle)
        xs.append(x)
        ss.append(x * (cycle + 1))
        xs.append(x)
        cycle += 2
        x += diff

print(sum([ss[20 + 40*x] for x in range((len(ss) - 20) // 40 + 1)]))

out = ""
for i in range(len(xs)):
    p = i % 40
    out += "#" if abs(p - xs[i]) < 2 else "."
    if p == 39:
        print(out)
        out = ""




