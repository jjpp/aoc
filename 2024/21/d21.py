#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


N = '789456123 0A'
D = ' ^A<v>'

d = {
    '^': -3,
    '>': 1,
    'v': 3,
    '<': -1,
}

def combos(a, b, ss):
    if len(a) == 0 and len(b) == 0:
        return ss

    out = []

    if len(a) > 0:
        out += combos(a[1:], b, [s + a[0] for s in ss])

    if len(b) > 0:
        out += combos(a, b[1:], [s + b[0] for s in ss])

    return out

def keep_shortest(ls):
    if len(ls) == 0:
        return []
    minl = min([len(s) for s in ls])
    return [l for l in ls if len(l) == minl]

m = {}

def shortest(kp, code):
    p = kp.index('A')
    out = ['']

    for c in code:
        pc = kp.index(c)
        if (p, pc) in m:
            co = m[p, pc]
        else:
            dx = pc % 3 - p % 3
            dy = (pc // 3) - (p // 3)
            cx = cy = ""

            if dy < 0:
                cy = '^' * abs(dy)
            else:
                cy = 'v' * abs(dy)

            if dx < 0:
                cx = '<' * abs(dx)
            else:
                cx = '>' * abs(dx)

            #co = [s + 'A' for s in combos(cx, cy, [''])]
            co = [ cx + cy + 'A', cy + cx + 'A' ]
            if kp[p + dx] == ' ':
                co.remove(cx + cy + 'A')
            if kp[p + 3*dy] == ' ':
                co.remove(cy + cx + 'A')

            m[p, pc] = co
        
        o2 = []
        for o in out:
            for coo in co:
                o2.append(o + coo)
        out = list(set(o2))

        p = pc

    return keep_shortest(out)


def try_all(kp, cs):
    o = []
    for code in cs:
        o += shortest(kp, code)
    return keep_shortest(o)

s = 0

for l in ls:
    k1 = try_all(N, [l])
    for i in range(25):
        k1 = try_all(D, k1)
        print(i, len(k1), len(k1[0]) if len(k1) > 0 else None, k1)

    cs = int(l[0:3]) * len(k1[0])
    s += cs
    print(s, cs, int(l[0:3]), len(k1[0]))
