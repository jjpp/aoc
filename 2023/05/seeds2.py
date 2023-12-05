#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

seeds = [int(i) for i in ls.pop(0).split()[1:]]

m = {}

ts = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def sorteddict(m):
    return { k: m[k] for k in sorted(m) }

while (len(ls) > 0):
    ls.pop(0)
    t = ls.pop(0).split()[0]
    m[t] = {}
    tm = {}
    while (len(ls) > 0 and ls[0] != ""):
        [dst, src, l] = [int(i) for i in ls.pop(0).split()]
        tm[src] = (dst - src, l)

    m[t] = sorteddict(tm)


def mapranges(t, rs):
    rs = sorteddict(rs)
    ro = {}

    # print(f"{rs}")
    # print(f"m[{t}] = {m[t]}")
    
    for r in rs:
        x = r
        l = rs[r]
        for k in m[t]:
            # print(f"checking ({x}, {l}) vs {k} -> {m[t][k]}")
            if l == 0:
                # print("empty range")
                break
            if x < k:
                # print("before k")
                if x + l < k:
                    # print("fits before k")
                    ro[x] = l
                    l = 0
                    break
                else:
                    # print("does not fit before k, splitting")
                    ro[x] = k - x
                    l = l - (k - x)
                    x = k
                    continue
            if x < (k + m[t][k][1]):
                # print("in k")
                if x + l < (k + m[t][k][1]):
                    # print("fits in k")
                    ro[x + m[t][k][0]] = l
                    l = 0
                    break
                else:
                    # print("does not fit into k, splitting")
                    ro[x + m[t][k][0]] = (k + m[t][k][1]) - x
                    l = l - ((k + m[t][k][1]) - x)
                    x = (k + m[t][k][1])
                    continue
        if l > 0:
            ro[x] = l

    return sorteddict(ro)

def locranges(rs):
    for t in ts:
        # rsold = rs
        rs = mapranges(t, rs)
        # print(f"{rsold} -> {rs}")
    return rs

rs = {}
while len(seeds) > 0:
    s = seeds.pop(0)
    l = seeds.pop(0)
    lrs = locranges({s: l})
    rs.update(lrs)

print(sorted(rs)[0])

