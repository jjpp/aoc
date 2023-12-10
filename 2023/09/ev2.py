#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def ep(vs):
    ds = []
    ds.append(vs)
    while True:
        ds.append([ds[-1][i + 1] - ds[-1][i] for i in range(0, len(ds[-1]) - 1)])
        s = sum([0 if x == 0 else 1 for x in ds[-1]])
        if s == 0:
            break

    for i in reversed(range(0, len(ds) - 1)):
        ds[i].insert(0, ds[i][0] - ds[i + 1][0])

    return ds[0][0]

print(sum([ep([int(i) for i in l.split()]) for l in ls]))


