#!/usr/bin/python3

import sys
import random

ls = [l.strip() for l in sys.stdin]

v = set()
e = {}

for l in ls:
    ks = l.split()
    ks[0] = ks[0][0:-1]

    v |= set(ks)

    for k in ks[1:]:
        e[ks[0], k] = 1


edges = list(e.keys())

def without_contractions():
    c = {}
    cs = {}
    for e in edges:
        if e[0] not in c:
            c[e[0]] = set([e[0]])
            cs[e[0]] = e[0]
        if e[1] not in c:
            c[e[1]] = set([e[1]])
            cs[e[1]] = e[1]
    return (c, cs)

# map of sets
(c, cs) = without_contractions()

eset = set(edges)

def edges_between(n1, n2):
    return [(k, l) for k in c[n1] for l in c[n2] if (k, l) in eset] + [(l, k) for k in c[n1] for l in c[n2] if (l, k) in eset]

# https://en.wikipedia.org/wiki/Karger%27s_algorithm

while True:
    while True:
        (n1, n2) = random.choice(list(edges))
        (n1, n2) = (cs[n1], cs[n2])
        if n1 != n2:
            break

    eb = edges_between(n1, n2)

    if len(c[n1]) > 3 and len(c[n2]) > 3 and len(eb) <= 3:
        continue

    for e in eb:
        eset.remove(e)

    c[n1] |= c[n2]
    del c[n2]
    for n in c[n1]:
        cs[n] = n1

    if len(c) == 2:
        if len(eset) <= 3:
            print("cut:", eset)
            print((len(v) - len(c[n1])) * len(c[n1]))
            exit(0)

        print("2 nodes with", len(eset), "edges, resetting")
        (c, cs) = without_contractions()
        eset = set(edges)
        
