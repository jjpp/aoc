#!/usr/bin/python3

import sys

f = [ set(list(x)) for (i, x) in enumerate([ 'cagedb', 'ab', 'gcdfa', 'fbcad', 'eafb', 'cdfbe', 'cdfgeb', 'dab', 'acedgfb', 'cefabd']) ]

def removewith(ws, ows):
    return set([w for w in ws if len(ows - set(list(w))) > 0])

def retainwith(ws, ows):
    print("retaining", ows, "in", ws)
    return set([w for w in ws if ows.issubset(set(list(w)))])

def allof(ws):
    return set(list("".join(ws)))

def fr(a, b):
    aw = ["".join(sorted(list(w))) for w in a]
    print(aw)
    d = []
    d.append(set([w for w in aw if len(w) == 6])) # 0
    d.append(set([w for w in aw if len(w) == 2])) # 1
    d.append(set([w for w in aw if len(w) == 5])) # 2
    d.append(set([w for w in aw if len(w) == 5])) # 3
    d.append(set([w for w in aw if len(w) == 4])) # 4
    d.append(set([w for w in aw if len(w) == 5])) # 5
    d.append(set([w for w in aw if len(w) == 6])) # 6 
    d.append(set([w for w in aw if len(w) == 3])) # 7
    d.append(set([w for w in aw if len(w) == 7])) # 8
    d.append(set([w for w in aw if len(w) == 6])) # 9


    _ef = allof(d[4]) - allof(d[1]) 
    _cg = allof(d[8]) - allof(d[1]) - allof(d[4]) - allof(d[7]) 
    _d = allof(d[7]) - allof(d[1])

    d[0] = removewith(d[0], _ef)
    d[6] = retainwith(set([x for x in d[6] if not x in d[0]]), _cg)
    d[9] = set([x for x in d[9] if not x in (d[0] | d[6])])

    _f = allof(d[8]) - allof(d[0])
    _e = _ef - _f
    _g = allof(d[8]) - allof(d[9])
    d[2] = retainwith(d[2], _g)
    _b = allof(d[1]) - allof(d[2])
    _a = allof(d[1]) - _b
    d[3] = retainwith(d[3] - d[2], _a)
    d[5] = d[5] - d[2] - d[3]

    out = 0
    for w in b:
        out *= 10
        w = "".join(sorted(list(w)))
        ns = [n for n in range(10) if w in d[n]]
        if len(ns) != 1:
            print(f"ERR: {d} -> {ns}")
            1 / 0
        out += ns[0]

    return out


total = 0
t2 = 0
for l in sys.stdin:
    l = l.strip()
    (a, b) = l.split(' | ')
    total += sum([1 for w in b.split(' ') if len(w) in { 2, 3, 7, 4 }])
    t2 += fr(a.split(), b.split())

print(total)
print(t2)
