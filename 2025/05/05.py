#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("\\d+", l)))


fresh = []
count = 0

for l in ls:
    ns = nums(l)
    if len(ns) > 1:
        fresh.append(ns)
    elif len(ns) == 0:
        fresh = sorted(fresh)
    else:
        isfresh = False
        for f in fresh:
            if f[0] <= ns[0] <= f[1]:
                isfresh = True
                break
        if isfresh:
            count += 1

print(count)

for i in range(0, len(fresh)):
    while True:
        found = False
        for j in range(0, len(fresh)):
            if i == j:
                continue

            if fresh[j][0] <= fresh[i][1] <= fresh[j][1]:
                fresh[i][1] = fresh[j][0] - 1
                found = True
        if not found:
            break

rs = 0
for f in fresh:
    if f[1] < f[0]:
        continue
    rs += f[1] - f[0] + 1

print(rs)

