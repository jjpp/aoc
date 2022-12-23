#!/usr/bin/python3

import sys
from collections import Counter

ls = [l.strip() for l in sys.stdin]

es = []

for r in range(len(ls)):
    for c in range(len(ls[r])):
        if ls[r][c] == '#':
            p = complex(c, r)
            es.append(p)

dirs = { 'N': -1j, 'NE': 1 - 1j, 'E': 1, 'SE': 1 + 1j, 'S': 1j, 'SW': -1 + 1j, 'W': -1, 'NW': -1 -1j }
plan = [ ('N', ['NE', 'N', 'NW']), ('S', ['SE', 'S', 'SW']), ('W', ['NW', 'W', 'SW']), ('E', ['NE', 'E', 'SE']) ]


def step(n, es):
    g = set(es)
    ne = {}
    
    def count_dirs(ds):
        return sum([1 for d in ds if e + dirs[d] in g])


    for e in es:
        if count_dirs(dirs) == 0:
            ne[e] = e
        else:
            ne[e] = e
            for pi in range(len(plan)):
                p = plan[(pi + n) % len(plan)]

                if count_dirs(p[1]) == 0:
                    ne[e] = e + dirs[p[0]]
                    break
   
    ts = Counter(ne.values())

    return [ne[e] if ts[ne[e]] == 1 else e for e in es]


def print_es(es):
    minx = int(min([e.real for e in es]))
    maxx = int(max([e.real for e in es]))
    miny = int(min([e.imag for e in es]))
    maxy = int(max([e.imag for e in es]))

    for r in range(miny, maxy + 1):
        out = ""
        for c in range(minx, maxx + 1):
            out += '#' if complex(c, r) in es else '.'
        print(out)

def get_free(es):
    minx = int(min([e.real for e in es]))
    maxx = int(max([e.real for e in es]))
    miny = int(min([e.imag for e in es]))
    maxy = int(max([e.imag for e in es]))

    return (maxx + 1 - minx) * (maxy + 1 - miny) - len(es)

def complex_key(x):
    return (x.real, x.imag)

i = 0
while True:
    nes = step(i, es)
    i += 1
    if sorted(nes, key = complex_key) == sorted(es, key = complex_key):
        break
    es = nes

print(i)

