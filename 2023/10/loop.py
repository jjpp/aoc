#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

g = {}
p = {}
dist = {}

c = {
        '|': [(0, -1), (0, 1)],
        '-': [(-1, 0), (1, 0)],
        '7': [(-1, 0), (0, 1)],
        'F': [(1, 0), (0, 1)],
        'L': [(0, -1), (1, 0)],
        'J': [(0, -1), (-1, 0)],
}

s = None
X = len(ls[0])
Y = len(ls)

for j in range(0, Y):
    for i in range(0, X):
        g[i, j] = ls[j][i]

for j in range(0, Y):
    for i in range(0, X):
        p[i, j] = []
        if g[i, j] == 'S':
            s = (i, j)
        elif g[i, j] == '.':
            ...
        else:
            for d in c[g[i, j]]:
                if i + d[0] in range(0, X) and j + d[1] in range(0, Y):
                    p[i, j].append((i + d[0], j + d[1]))


for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    i = s[0] + d[0]
    j = s[1] + d[1]
    if (i, j) in g and s in p[(i, j)]:
        p[s].append((i, j))

dist[s] = 0
check = [s]

m = 0

while len(check) > 0:
    new_check = []
    for c in check:
        for c2 in p[c]:
            if c in p[c2]:
                if c2 in dist:
                    print(f"{c} -> {c2}: {dist[c2]} vs {dist[c]}")
                    m = max(m, dist[c], dist[c2])
                else:
                    dist[c2] = dist[c] + 1
                    new_check.append(c2)
    check = new_check

print(m)

        


