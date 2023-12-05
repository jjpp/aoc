#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

seeds = [int(i) for i in ls.pop(0).split()[1:]]

m = {}

ts = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

while (len(ls) > 0):
    ls.pop(0)
    t = ls.pop(0).split()[0]
    m[t] = {}
    tm = {}
    while (len(ls) > 0 and ls[0] != ""):
        [dst, src, l] = [int(i) for i in ls.pop(0).split()]
        tm[src] = (dst - src, l)

    m[t] = { k: tm[k] for k in sorted(tm.keys()) }


def mapx(t, x):
    # print(f"mapx {t} {x} {m[t]}")
    for k in m[t]:
        # print(f"{k}, {x}, {k + m[t][k][1]} {m[t][k]}")
        if x < k:
            # print("too small")
            return x
        if x < (k + m[t][k][1]):
            # print("in range")
            return x + m[t][k][0]
    return x


def loc(x):
    for t in ts:
        # xold = x
        x = mapx(t, x)
        # print(f"{t} {xold} -> {x}")
        # print()

    return x
        

print(min([loc(s) for s in seeds]))


