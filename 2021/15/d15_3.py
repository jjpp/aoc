#!/usr/bin/python3

import sys
from queue import PriorityQueue

lns = [l.strip() for l in sys.stdin]

g = {}
Y = len(lns)
X = len(lns[0])

def w(c, i):
    return (int(c) - 1 + i) % 9 + 1

for (row, l) in enumerate(lns):
    for (pos, c) in enumerate(l):
        for dx in range(5):
            for dy in range(5):
                g[pos + dx * X, row + dy * Y] = w(c, dx + dy)

def nrs(p):
    return [(p[0] + dx, p[1] + dy) for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] if (p[0] + dx, p[1] + dy) in g]

s = {}
s[0, 0] = 0


q = PriorityQueue()
q.put((0, (0, 0)))

count = 0

while not q.empty() and (X * 5 - 1, Y * 5 - 1) not in s:
    (d, p) = q.get()
    for pn in nrs(p):
        if not pn in s or s[p] + g[pn] < s[pn]:
            s[pn] = s[p] + g[pn]
            q.put((s[pn], pn))
            count += 1

print(count)


print(s[X * 5 - 1, Y * 5 - 1])
    
