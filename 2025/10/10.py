#!/usr/bin/python3

import sys
import re
from queue import PriorityQueue
from collections import Counter
from pulp import *

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

s = 0

def target(t):
    tx = 0
    for i in list(reversed(list(t[1:-1]))):
        tx *= 2
        if i == '#':
            tx += 1
    return tx

def button(b):
    bx = 0
    for n in nums(b):
        bx += 2 ** n
    return bx

def tries(t, bs, pushed):
    if len(bs) == 0:
        return pushed if t == 0 else 99999

    return min(tries(t, bs[1:], pushed), tries(t ^ bs[0], bs[1:], pushed + 1))

for l in ls:
    l = l.split(' ')
    t = target(l[0])
    bs = list(map(button, l[1:-1]))
    s += tries(t, bs, 0)

print(s)

def tries6(t, bs):
    a = [ [] for x in t ]
    for b in bs:
        for i in range(len(t)):
            a[i].append(1 if i in b else 0)

    mt = max(t)

    xs = []
    ss = 0
    for i in range(len(bs)):
        xs.append(LpVariable("x" + str(i), 0, mt, LpInteger))
        ss += xs[-1]

    p = LpProblem("minimize", LpMinimize)
    sv = LpVariable("ss", max(t), sum(t), LpInteger)
    p += (sv == ss)

    for i in range(len(t)):
        lhs = 0
        for j in range(len(bs)):
            if i in bs[j]:
                lhs += xs[j]
        p += (lhs == t[i])

    p.setObjective(sv)
    status = p.solve(PULP_CBC_CMD(msg = False))
    s = sv.varValue
    
    return int(s)

s = 0
for l in ls:
    bl = {}
    l = l.split(' ')
    t = nums(l[-1])
    bs = list(sorted(map(nums, l[1:-1])))

    s += tries6(t, bs)
print(s)
