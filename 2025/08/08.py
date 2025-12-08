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

for i in range(N - 1):
    for j in range(i + 1, N):
        d[i, j] = math.dist(ls[i], ls[j])

for i in range(N):
    cs[i] = set([i])
    csm[i] = i

sds = list(sorted(d.values()))

steps = 10
steps = 1000 if len(ls) > 20 else 10
step = 0

for sd in sds:
#    print(f"joining with distance {sd}")
    ks = [k for k in d if d[k] == sd]
    print([ks], "@", step)
    if len(ks) > 1:
        print("Non-unique distance", ks)
    (k1, k2) = ks[0]

#    print("Boxes: ", ls[k1], ls[k2])
#    print(f"Adding from {k2} to {k1}")
#    print(f"       from {csm[k2]} to {csm[k1]}")

    if csm[k2] < csm[k1]:
        (k1, k2) = (k2, k1)

    if csm[k1] != csm[k2]:
        cs[csm[k1]] |= cs[csm[k2]]
        ck2 = cs[csm[k2]]
        csmk2 = csm[k2]
        cs[csm[k2]] = set()
        for k in ck2:
            csm[k] = csm[k1]

        if len(cs[csm[k1]]) == N:
            print(ls[k1][0] * ls[k2][0])
            break
#    else:
#        print("Already in the same circuit")

    step += 1
    if steps == step: 
        sizes = list(reversed(sorted([len(x) for x in cs.values() if len(x) > 0 ])))
        print(sizes[0] * sizes[1] * sizes[2])

