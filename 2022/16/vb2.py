#!/usr/bin/python3

# slower version of second part.
# did not manage to go through the state space
# in 40 minutes on a random i5 t480 laptop
# yet, the best was printed out in a few minutes

import sys
from queue import PriorityQueue
from copy import deepcopy

ls = [l.strip() for l in sys.stdin]

g = {} # flows
e = {} # edges

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
best = 0

def step(n, o, t, y, e, yt, et, f, p):
    global best
    if t > 25:
        return

    o_ = deepcopy(o)
    o_[n] = 'y' if n == y else 'e'
    f += (26 - t) * g[n]

    # statespace key: (open valves + who opened each) + my and elephant's positions
    key = "".join([k + o_[k] for k in sorted(o_)]) + y + e
    if not key in best_for or f > best_for[key]:
#        print(f, key, n, y, e, yt, et, t, ", ".join([i[1] + "@" + str(i[0]) for i in p]))
        best_for[key] = f
        if f > best:
            best = f
            print(best, key)
    else:
#        print("prune: ", f, key, ", ".join([i[1] + "@" + str(i[0]) for i in p]))
        return

    for n2 in d[y]:
        if n2 not in o_:
            step(n2, o_, yt + 1 +  d[y][n2], n2, e, yt + 1 +  d[y][n2], et, f, sorted(p + [(yt + 1 +  d[y][n2], f'y:{n2}')]))

    for n2 in d[e]:
        if n2 not in o_:
            step(n2, o_, et + 1 +  d[e][n2], y, n2, yt, et + 1 +  d[e][n2], f, sorted(p + [(et + 1 +  d[e][n2], f'e:{n2}')]))

step('AA', {}, 0, 'AA', 'AA', 0, 0, 0, [])


print(max(best_for.values()))


