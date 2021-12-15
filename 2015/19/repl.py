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


def generation(m, vs):
    for (k, v) in rs.items():
        try:
            i = m.index(k)
            while True:
                vs |= { m[0:i] + e + m[i+len(k):] for e in v }
                i = m.index(k, i + 1)
        except ValueError:
            # ignore
            ...

    return vs

old = set(['e'])
seen = set()
count = 0

while True:
    count += 1
    print(count, len(old), len(seen))
    new = set()
    for tm in old:
        new = generation(tm, new)
        new -= seen

    if m in new:
        break

    seen |= old
    old = set(new - seen)

print(count)
