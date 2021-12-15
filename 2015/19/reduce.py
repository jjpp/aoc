#!/usr/bin/python3

import sys

rs = {}
rx = {}
m = ""


for l in sys.stdin:
    l = l.strip()
    if " => " in l:
        [a, _, b] = l.split(' ')
        rx[b] = a
        if not a in rs:
            rs[a] = set()
        rs[a] |= set([b])
    elif len(l) > 0:
        m = l

byl = list(rx.keys())
byl.sort(key=len)
seen = set()

def reduce(o):
    new = set()
    for m in o:
        for b in byl:
            if b in m:
                i = m.index(b)
                new |= ({ m[0:i] + rx[b] + m[i+len(b):] } - seen)

    return new

old = { m }

count = 0
while True:
    count += 1
    ml = min([len(s) for s in old])
    print(count, len(old), len(seen), ml)
    n = reduce(old)
    if "e" in n:
        break
    n = {s for s in n if len(s) <= ml + 1}
    seen |= old
    old = n

print(count)

