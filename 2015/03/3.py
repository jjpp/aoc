#!/usr/bin/python3

import sys

l = sys.stdin.readline()

x = 0
y = 0
m = {}

m[0, 0] = 1

for c in l:
    if c == '<':
        x -= 1
    elif c == '>':
        x += 1
    elif c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    m[x, y] = m.get((x, y), 0) + 1

print(len(m))

