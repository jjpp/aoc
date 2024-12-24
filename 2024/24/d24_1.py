#!/usr/bin/python3

# somewhat cleaned p1

import sys, re

ls = [l.strip() for l in sys.stdin]

vs = {}

for l in range(ls.index('')):
    (var, val) = ls[l].split(': ')
    vs[var] = int(val)

ops = {
        'XOR': lambda a, b: lambda: g(a) ^ g(b),
        'OR':  lambda a, b: lambda: g(a) | g(b),
        'AND': lambda a, b: lambda: g(a) & g(b),
}

def g(v):
    if not isinstance(vs[v], int):
        vs[v] = vs[v]()
    return vs[v]

    
for l in range(ls.index('') + 1, len(ls)):
    (a, op, b, _, r) = ls[l].split(' ')
    vs[r] = ops[op](a, b)

out = 0
for z in reversed(sorted([v for v in vs.keys() if v[0] == 'z'])):
    out *= 2
    out += g(z)

print(out)
