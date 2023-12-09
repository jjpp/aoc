#!/usr/bin/python3

import sys
from math import prod, lcm

ls = [l.strip() for l in sys.stdin]

cmds = ls.pop(0)
ls.pop(0)

t = {}

for l in ls:
    d = l.split()
    k = d[0]
    l = d[2][1:-1]
    r = d[3][:-1]
    t[k] = (l, r)

ks = [k for k in t if k[2] == 'A']
c = 0

def allz(ks):
    return sum([1 if k[2] == 'Z' else 0 for k in ks]) == len(ks)

def steps(k):
    ok = k
    c = 0
    zs = []
    seen = {}
    while True:
        cmd = cmds[c % len(cmds)]
        key = k + str(c % len(cmds))
        if key in seen:
            break
        seen[key] = c
        if cmd == 'L':
            k = t[k][0]
        else:
            k = t[k][1]
        c += 1
        if k[2] == 'Z':
            zs.append(c)

    return (c, key, seen[key], zs)

print(ks)

a = []
n = []

print(len(cmds))

for k in ks:
    s = steps(k)
    print(s)
    n.append(s[0] - s[2])
    a.append(s[3][0] - n[-1])

def solve(a, a2, n, n2, j):
    for i in range(0, int(n / (277 ** j))):
        if (a + i * n) % n2 == a2:
            return a + i*n
    raise ValueError(f"could not solve {a}, {n}, {n2}")


print(a)
print(n)

if sum([0 if a_ == 0 else 1 for a_ in a]) == 0:
    print(lcm(*n))
else:
    print("Do solve")
    for i in range(0, len(a)):
        print(f"x = {a[i]} mod {n[i]}")


