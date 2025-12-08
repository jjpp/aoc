#!/usr/bin/python3

import sys
import re
import math

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

cs = dict()
N = len(ls)
d = dict()
csm = dict()

for i in range(N):
    ls[i] = nums(ls[i])

keyof = dict()

for i in range(N - 1):
    for j in range(i + 1, N):
        d[i, j] = math.dist(ls[i], ls[j])
        if d[i, j] in keyof:
            print("Non-unique distance ", d[i, j])
        keyof[d[i, j]] = (i, j)

for i in range(N):
    cs[i] = set([i])
    csm[i] = i

sds = list(sorted(d.values()))

steps = 1000 if len(ls) > 20 else 10
step = 0

for sd in sds:
    (k1, k2) = keyof[sd]

    if csm[k1] != csm[k2]:
        if csm[k2] < csm[k1]:
            (k1, k2) = (k2, k1)

        cs[csm[k1]] |= cs[csm[k2]]
        ck2 = cs[csm[k2]]
        csmk2 = csm[k2]
        del cs[csm[k2]]

        for k in ck2:
            csm[k] = csm[k1]

        if len(cs) == 1:
            print(ls[k1][0] * ls[k2][0])
            break

    step += 1
    if steps == step: 
        sizes = list(reversed(sorted([len(x) for x in cs.values() if len(x) > 0 ])))
        print(sizes[0] * sizes[1] * sizes[2])

