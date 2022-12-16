#!/usr/bin/python3

# working attempt for the first half.

import sys
from queue import PriorityQueue
from copy import deepcopy

ls = [l.strip() for l in sys.stdin]

g = {} # flows
e = {} # edges

s['AA'] = 0

for l in ls:
    # Valve IK has flow rate=6; tunnels lead to valves EU, XY, AD, SC, CH
    d_ = l.split(' ', 9)
    v = d_[1]
    r = int(d_[4][5:-1])
    g[v] = r
    e[v] = d_[9].split(', ')
    d[v] = { t: 1 for t in e[v] }

nodes = [v for v in g if g[v] > 0]
nodes += ['AA']
d = {}

def dists(v):
    q = PriorityQueue()
    d = {v: 0}
    q.put((v, 0))

    while not q.empty():
        (n, _) = q.get()
        for t in e[n]:
            if t not in d or d[t] > d[n] + 1:
                d[t] = d[n] + 1
                q.put((t, d[t]))

    return { n: d[n] for n in nodes }

for n in nodes:
    d[n] = dists(n)

best_for = {}

def step(n, o, t, p, f):
    if t > 29:
        return

    o_ = [*o, n]
    f += (30 - t) * g[n]
    p = [*p, n]

    key = "".join(sorted(o_))
    if not key in best_for or f > best_for[key]:
        best_for[key] = f
    else:
        return

    for n2 in d[n]:
        if n2 not in o_:
            step(n2, o_, t + 1 +  d[n][n2], p, f)

step('AA', [], 0, [], 0)


print(max(best_for.values()))


