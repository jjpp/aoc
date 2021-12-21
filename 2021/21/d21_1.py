#!/usr/bin/python3

import sys

(a, b) = [int(l.strip().split(' ')[4]) for l in sys.stdin]


d = 100
dc = 0
p = 0
ascore = bscore = 0
print(a, b)

while ascore < 1000 and bscore < 1000:
    for _ in range(3):
        dc += 1
        d += 1
        d = (d - 1) % 100 + 1
        a = (a - 1 + d) % 10 + 1

    ascore += a
    print(a, d, ascore, dc)

    (a, b) = (b, a)
    (ascore, bscore) = (bscore, ascore)

print(a, b)
print(ascore, bscore)
print(dc)

print(ascore * dc)
