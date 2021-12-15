#!/usr/bin/python3

import sys

l = sys.stdin.readline()

x = [0, 0]
y = [0, 0]
m = {}

m[0, 0] = 1
z = 0

for c in l:
    if c == '<':
        x[z] -= 1
    elif c == '>':
        x[z] += 1
    elif c == '^':
        y[z] += 1
    elif c == 'v':
        y[z] -= 1
    m[x[z], y[z]] = m.get((x[z], y[z]), 0) + 1
    z = 1 - z

print(len(m))

