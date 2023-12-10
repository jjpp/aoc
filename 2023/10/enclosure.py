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

sd = []

for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    i = s[0] + d[0]
    j = s[1] + d[1]
    if (i, j) in g and s in p[(i, j)]:
        p[s].append((i, j))
        sd.append(d)

for d in c:
    if sorted(c[d]) == sorted(sd):
        s_ = d

g[s] = s_

dist[s] = 0
check = [s]

m = 0

while len(check) > 0:
    new_check = []
    for c in check:
        for c2 in p[c]:
            if c in p[c2]:
                if c2 in dist:
                    m = max(m, dist[c], dist[c2])
                else:
                    dist[c2] = dist[c] + 1
                    new_check.append(c2)
    check = new_check

print(m)

check = [c for c in dist if dist[c] == m]

while len(check) > 0:
    new_check = []
    for c in check:
        for c2 in p[c]:
            if c in p[c2]:
                if dist[c2] < dist[c]:
                    dist[c2] = dist[c]
                    new_check.append(c2)
    check = new_check

sides = {
        ('|', (0, 1)): [[(1, 0)], [(-1, 0)]],
        ('|', (0, -1)): [[(-1, 0)], [(1, 0)]],
        ('-', (1, 0)): [[(0, -1)], [(0, 1)]],
        ('-', (-1, 0)): [[(0, 1)], [(0, -1)]],
        ('L', (0, -1)): [[(0, 1), (-1, 0)], []],
        ('L', (1, 0)): [[], [(0, 1), (-1, 0)]],
        ('7', (-1, 0)): [[], [(1, 0), (0, -1)]],
        ('7', (0, 1)): [[(0, -1), (1, 0)], []],
        ('J', (-1, 0)): [[(1, 0), (0, 1)], []],
        ('J', (0, -1)): [[], [(1, 0), (0, 1)]],
        ('F', (1, 0)): [[(-1, 0), (0, -1)], []],
        ('F', (0, 1)): [[], [(-1, 0), (0, -1)]],
}

c = s
seen = set()
left = set()
right = set()
outer = None

while True:
    seen.add(c)
    ns = [n for n in p[c] if n not in seen and n != s]
    if len(ns) == 0:
        break
    n = ns[0]
    d = (n[0] - c[0], n[1] - c[1])

    for side in sides[g[c], d][0]:
        s_ = (c[0] + side[0], c[1] + side[1])
        if s_ in g and dist.get(s_, None) != m:
            left.add(s_)

    for side in sides[g[c], d][1]:
        s_ = (c[0] + side[0], c[1] + side[1])
        if s_ in g and dist.get(s_, None) != m:
            right.add(s_)

    c = n

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def fill(s):
    global outer
    c = set(s)
    while len(c) > 0:
        new_c = set()
        for x in c:
            for d in dirs:
                x2 = (x[0] + d[0], x[1] + d[1])
                if x2 not in g:
                    if outer == None or outer == s: 
                        outer = s
                    else:
                        print("Outer cannot be left and right at the same time?")
                        exit(1)

                if x2 not in g or x2 in s or dist.get(x2, None) == m:
                    continue
                s.add(x2)
                new_c.add(x2)
        c = new_c

fill(right)
fill(left)

print(len(right) if outer == left else len(left))
