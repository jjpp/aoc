#!/usr/bin/python3

# part 1

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

ts = set()

for (a, b) in ps:
    for c in ns:
        if c != a and c != b and (a, c) in ps and (b, c) in ps:
            if c[0] == 't':
                ts.add(tuple(sorted([a, b, c])))

print(len(ts))

