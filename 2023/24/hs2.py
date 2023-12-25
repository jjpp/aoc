#!/usr/bin/python3

import sys
from sympy import var, Eq, solve

ls = [l.strip() for l in sys.stdin]

ps = []
vs = []

for l in ls:
    (p, v) = l.split(' @ ')
    ps.append([int(x) for x in p.split(', ')])
    vs.append([int(x) for x in v.split(', ')])

xyz = "xyz"

s = [var("s" + xyz[i]) for i in range(0, 3)] 
v = [var("v" + xyz[i]) for i in range(0, 3)] 

sys = []

t = []

for i in range(0, 3):
    t.append(var("t" + str(i)))
    for j in range(0, 3):
        sys.append(Eq(s[j] + v[j]*t[i], ps[i][j] + t[i] * vs[i][j]))

solutions = solve(sys)

print(solutions)


print(sum([solutions[0][s[i]] for i in range(0, 3)]))

