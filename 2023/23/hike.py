#!/usr/bin/python3

import sys
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]


g = {}

X = len(ls[0])
Y = len(ls)

dirs = {
        '>': (1, 0),
        '<': (-1, 0),
        'v': (0, 1),
        '^': (0, -1)
}


S = (ls[0].index('.'), 0)
E = (ls[-1].index('.'), Y - 1)

p = []

p.append(S)
for y in range(1, Y - 1):
    for x in range(1, X - 1):
        if ls[y][x] == '.':
            d = sum([1 if ls[y + dy][x + dx] != '#' else 0 for (dx, dy) in dirs.values()])
            if d > 2:
                p.append((x, y))

p.append(E)

print(p)
print(len(p))

for y in range(0, Y):
    for x in range(0, X):
        g[x, y] = ls[y][x]

def dists(a):
    q = PriorityQueue()
    ds = {}

    q.put((0, a))

    out = {}

    print("checking ", a)

    while not q.empty():
        (d, (x, y)) = q.get()
        print(d, x, y)

        if (x, y) not in g or g[x, y] == '#' or ((x, y) in ds and ds[x, y] <= d):
            continue

        ds[x, y] = d

        if (x, y) in p and (x, y) != a:
            out[(x, y)] = ds[x, y]
        else:
            if g[x, y] == '.':
                for d_ in dirs.values():
                    q.put((d + 1, (x + d_[0], y + d_[1])))
            else:
                q.put((d + 1, (x + dirs[g[x, y]][0], y + dirs[g[x, y]][1])))

    print("found", out)
    return out

dp = {}
for i in range(0, len(p)):
    dp[p[i]] = dists(p[i])

def longest(a, dist, seen):
    if a == E:
        return dist

    return max([longest(b, dist + dp[a][b], seen | set([b])) for b in dp[a] if b not in seen])

print(longest(S, 0, set()))
