#!/usr/bin/python3

import sys, re

ls = [l.strip() for l in sys.stdin]

ns = set()
ps = set()

for l in ls:
    (a, b) = l.split('-')
    ps.add((a, b))
    ps.add((b, a))
    ns.add(a)
    ns.add(b)

cs = set()

sns = sorted(list(ns))

for a in sns:
    c = set([a])
    for b in sns:
        if all([(a, b) in ps for a in c]):
            c.add(b)
    cs.add(",".join(list(sorted(c))))


maxlen = max([len(c) for c in cs])
for c in cs:
    if len(c) == maxlen:
        print(c)

