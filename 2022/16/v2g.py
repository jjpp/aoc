#!/usr/bin/python3

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

print("digraph {")
for f in g:
    print(f"{f} [label=\"{f}: {g[f]}\"]")
    for t in e[f]:
        print(f, "->", t)
print("}")

