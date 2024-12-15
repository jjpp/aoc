#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])*2
Y = ls.index("")
cmds = "".join(ls[Y+1:])

for y in range(Y):
    if "@" in ls[y]:
        p = ls[y].index("@")*2 + 1j*y

ds = {
        '<': -1,
        '>': 1,
        '^': -1j,
        'v': 1j
}

for y in range(Y):
    tr = {
        '.': '..',
        '#': '##',
        'O': '[]',
        '@': '..',
    }
    nls = ""
    for c in ls[y]:
        nls += tr[c]
    ls[y] = list(nls)

def g(p):
    return ls[int(p.imag)][int(p.real)]

def setg(p, v):
    ls[int(p.imag)][int(p.real)] = v

def printg(p):
    for y in range(Y):
        l = [*ls[y]]
        if int(p.imag) == y:
            l[int(p.real)] = '@'
        print("".join(l))

def gs(ps):
    return [g(p) for p in ps]

def step(p, d):
    np = p + ds[d]
    if g(np) == '.':
        p = np
        #print("free step")
    elif g(np) == '#':
        p = p
        #print("wall")
    elif g(np) in '[]':
        if d in '<>': 
            lp = np
            #print("block")
            while g(lp) in '[]':
                lp = lp + ds[d]
            #print("behind it: ", lp, g(lp))
            if g(lp) == '.':
                while lp != np:
                    setg(lp, g(lp - ds[d]))
                    lp -= ds[d]
                setg(np, '.')
                p = np
        else:
            tops = [np, np + (1 if g(np) == '[' else -1)]
            repl = {t: '.' for t in tops}
            move = set(tops)
            tops_ = gs(tops)
            while all([t in '[].' for t in tops_]) and any([t in '[]' for t in tops_]):
                ntops = []
                for t in tops:
                    if g(t) == '.':
                        ntops.append(t)
                    elif g(t) in '[]':
                        dh = 1 if g(t) == '[' else -1
                        ntops.append(t + ds[d])
                        ntops.append(t + ds[d] + dh)
                        move.add(t)
                        move.add(t + dh)
                        if '#' in gs(ntops[-2:]):
                            return p
                        repl[t + ds[d]] = g(t)
                        repl[t + ds[d] + dh] = g(t + dh)
                tops = list(set(ntops))
                move |= set(tops)
                tops_ = gs(tops)
            #print('vertical: ', tops, tops_)
            #print(repl)
            #print(move, move - set(repl.keys()))
            for (r, v) in repl.items():
                setg(r, v)
            for m in move - set(repl.keys()):
                setg(m, '.')
            setg(np, '.')
            p = np
    return p

for c in cmds:
    p = step(p, c)
    #printg(p)
    #print(p, c)
    #print()

s = 0
for y in range(Y):
    for x in range(X):
        if ls[y][x] == '[':
            s += 100*y + x

print(s)

