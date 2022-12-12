#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

g = {}

Y = len(ls)
X = len(ls[0])

S = E = None


for y in range(Y):
    for x in range(X):
        h = ls[y][x]
        if h == 'S':
            S = complex(x, y)
            h = 'a'
        elif h == 'E':
            E = complex(x, y)
            h = 'z'

        g[complex(x, y)] = ord(h) - ord('a')



steps = {}
check = {S}
steps[S] = 0

dirs = [1, -1, -1j, 1j]

while len(check) > 0:
    p = check.pop()

    for d in dirs:
        if p + d not in g:
            continue

        if g[p + d] <= g[p] + 1 and (p + d not in steps or steps[p + d] > steps[p] + 1):
            steps[p + d] = steps[p] + 1
            check.add(p + d)

print(steps[E])

        
        


