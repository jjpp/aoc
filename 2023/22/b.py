#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

bs = []
ds = {}
os = {}

for l in ls:
    (a,b) = l.split('~')
    bs.append(([int(i) for i in a.split(',')], [int(i) for i in b.split(',')]))

g = {}


def fall(b, bi):
    lx = abs(b[0][0] - b[1][0])
    ly = abs(b[0][1] - b[1][1])
    lz = abs(b[0][2] - b[1][2])
    l = max(lx, ly, lz) + 1

    dx = 0 if b[0][0] == b[1][0]  else (b[1][0] - b[0][0]) // lx
    dy = 0 if b[0][1] == b[1][1]  else (b[1][1] - b[0][1]) // ly
    dz = 0 if b[0][2] == b[1][2]  else (b[1][2] - b[0][2]) // lz

    ds[bi] = (dx, dy, dz, l)


    (x, y) = (b[0][0], b[0][1])
    z = min(b[0][2], b[1][2])


    while z > 1 and all([(x + i*dx, y + i*dy, z - 1) not in g for i in range(0, l)]):
        z -= 1

    os[bi] = (x, y, z)

    for i in range(0, l):
        g[x + dx*i, y + dy * i, z + abs(dz) * i] = bi

bs = sorted(bs, key = lambda b: min(b[0][2], b[1][2]))

for bi in range(0, len(bs)):
    b = bs[bi]
    fall(b, bi)

def get_ab(i, dl):
    (x, y, z) = os[i]
    (dx, dy, dz, l) = ds[i]
    others = set([g.get((x + dx*i_, y + dy*i_, z + dz*i_ + dl), i) for i_ in range(0, l)])
    if i in others:
        others.remove(i)
    return others


def can_remove(i):
    above = get_ab(i, 1)

    can_remove = True

    for j in above:
        below = get_ab(j, -1)
        below.remove(i)
        can_remove = can_remove and len(below) > 0

    return can_remove

all_ab_cache = {}

def all_ab(i, dl):
    if (i, dl) in all_ab_cache:
        return all_ab_cache[i, dl]
    others = get_ab(i, dl)
    o = set(others)
    for j in others:
        o |= all_ab(j, dl)
    all_ab_cache[i, dl] = o
    return o

def supports(i):
    above = all_ab(i, 1)
    below = all_ab(i, -1) | set([i])
    
    return sum([1 if len(all_ab(j, -1) - below - above) == 0 else 0 for j in above])

        
print(sum([1 if can_remove(i) else 0 for i in range(0, len(bs))]))
print(sum([supports(i) for i in range(0, len(bs))]))


