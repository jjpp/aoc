#!/usr/bin/python3

import sys

rs = {}
m = ""

for l in sys.stdin:
    l = l.strip()
    if " => " in l:
        [a, _, b] = l.split(' ')
        if not a in rs:
            rs[a] = set()
        rs[a] |= set([b])
    elif len(l) > 0:
        m = l

vs = set()

for (k, v) in rs.items():
    print(k, v)
    try:
        i = m.index(k)
        while True:
            vs |= set([m[0:i] + e + m[i+len(k):] for e in v])
            i = m.index(k, i + 1)
    except ValueError:
        # ignore
        ...

print(rs)
print(vs)
print(len(vs))

            

