#!/usr/bin/python3

import sys

lns = [int(x) for x in sys.stdin.readline().strip().split(',')]


spends = [0]

for a in range(1, max(lns) - min(lns) + 1):
    spends.append(a + spends[-1])

spend_min = sum(lns)
min2 = 9999999999999999
for x in range(min(lns), max(lns) + 1):
    spend_min = min(spend_min, sum([abs(x - n) for n in lns]))
    min2 = min(min2, sum([spends[abs(x - n)] for n in lns]))


print(spend_min)
print(min2)

