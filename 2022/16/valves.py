#!/usr/bin/python3

# initial attempt that went nowhere

import sys
from queue import PriorityQueue
from copy import deepcopy

ls = [l.strip() for l in sys.stdin]

g = {} # flows
b = {} # best so far?
e = {} # edges
s = {} # 
o = {} # open valves at 
d = {}

s['AA'] = 0

for l in ls:
    # Valve IK has flow rate=6; tunnels lead to valves EU, XY, AD, SC, CH
    d_ = l.split(' ', 9)
    v = d_[1]
    r = int(d_[4][5:-1])
    g[v] = r
    e[v] = d_[9].split(', ')
    d[v] = { t: 1 for t in e[v] }

max_open = len([g[v] for v in g if g[v] > 0])
print(max_open)
best = 0

if False:
    zeros = [v for v in g if g[v] == 0]
    zeros.remove('AA')

    while len(zeros) > 0:
        rv = zeros.pop()
        for v in g:
            if rv in e[v]:
                e[v].remove(rv)
                e[v] += e[rv]
                for t in d[rv]:
                    d[v][t] = min(d[v].get(t, 3000), d[rv][t])

sol = 'AADDCCBBAAIIJJIIAADDEEFFGGHHGGFFEEDDCC'

def step(v, t, flow, o, p, kf, shall_open):
    def dump():
        print(flow, 'at', v)
        print(p)
        print(sorted(o))
        print(kf)

    global best

    if best < flow:
        dump()

    best = max(best, flow)
    if t >= 29:
        return

    kf = deepcopy(kf)


    if v not in kf or kf[v] < flow:
        kf[v] = flow
    else:
        if sol.startswith("".join(p)):
            print("returning")
            dump()
        return

    p = [*p, v]

    if shall_open and not v in o and g[v] > 0:
        t += 1
        flow += (30 - t) * g[v]
        o = [*o, v]
        kf[v] = flow

    if best < flow:
        dump()

    best = max(best, flow)
    if t >= 30:
        return

    if len(o) == max_open:
        return

    for tv in e[v]:
        step(tv, t + d[v][tv], flow, o, p, kf, True)
        step(tv, t + d[v][tv], flow, o, p, kf, False)


step('AA', 0, 0, [], [], {}, False)

print(best)

