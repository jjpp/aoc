#!/usr/bin/python3

import sys
import re
from math import prod

ls = [l for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

last = len(ls) - 1
lsn = []

for i in range(last):
    lsn.append(nums(ls[i]))

s = 0
ops = ls[last].split()

for i in range(len(lsn[0])):
    ns = [lsn[j][i] for j in range(last)]
    if ops[i] == '+':
        part = sum(ns)
    else:
        part = prod(ns)

    s += part
print(s)

p2 = 0
ns = []
for i in range(len(ls[0]) - 1, -1, -1):
    col = "".join([ls[j][i] if len(ls[j]) > i else " " for j in range(last)])
    op = ls[last][i] if len(ls[last]) > i else " "
    ns += nums(col)
    if op == '+':
        part = sum(ns)
        p2 += part
        ns = []
    if op == '*':
        part = prod(ns)
        p2 += part
        ns = []

print(p2)

