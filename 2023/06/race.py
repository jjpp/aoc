#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

times = [int(x) for x in ls[0].split()[1:]]
dists = [int(x) for x in ls[1].split()[1:]]

def wtw(time, dist):
    wins = [s * (time - s) for s in range(0, time + 1) if s * (time - s) > dist]
    return len(wins)

ws = [wtw(times[i], dists[i]) for i in range(0, len(times))]

p = 1
for w in ws:
    p *= w

print(p)

t = int("".join(ls[0].split()[1:]))
d = int("".join(ls[1].split()[1:]))

print(wtw(t, d))
