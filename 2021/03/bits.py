#!/usr/bin/python3

import sys

bits = [0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0]
count = 0

for l in sys.stdin:
    l = l.strip()
    for (i, b) in enumerate(l):
        bits[i] = int(b) + (bits[i] if len(bits) > i else 0)
    count += 1

e = [1 if b*2 > count else 0 for b in bits]
g = [0 if b*2 > count else 1 for b in bits]


epsilon = int("".join([str(i) for i in e]), 2)
gamma = int("".join([str(i) for i in g]), 2)

print (epsilon * gamma)



