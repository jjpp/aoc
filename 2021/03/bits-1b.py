#!/usr/bin/python3

import sys

bits = []
count = 0

for l in sys.stdin:
    l = l.strip()
    for (i, b) in enumerate(l):
        while len(bits) <= i:
            bits += [0]
        bits[i] += int(b)
    count += 1

e = [1 if b*2 > count else 0 for b in bits]
g = [0 if b*2 > count else 1 for b in bits]


epsilon = int("".join([str(i) for i in e]), 2)
gamma = int("".join([str(i) for i in g]), 2)

print (epsilon * gamma)



