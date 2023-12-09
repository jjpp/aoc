#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

cmds = ls.pop(0)
ls.pop(0)

t = {}

for l in ls:
    d = l.split()
    k = d[0]
    l = d[2][1:-1]
    r = d[3][:-1]
    t[k] = (l, r)

k = 'AAA'
c = 0
while k != 'ZZZ':
    if cmds[c % len(cmds)] == 'L':
        k = t[k][0]
    else:
        k = t[k][1]
    c += 1

print(c)

