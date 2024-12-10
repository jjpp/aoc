#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

heads = []

for j in range(Y):
    for i in range(X):
        if ls[j][i] == '0':
            heads.append((i, j))

def in_grid(x, y):
    return 0 <= x < X and 0 <= y < Y

def find_trails(p):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ps = {p}
    for step in range(1, 10):
        s_ = str(step)
        ps_new = set()
        for p_ in ps:
            for d in dirs:
                pn = (p_[0] + d[0], p_[1] + d[1])
                if in_grid(*pn) and ls[pn[1]][pn[0]] == s_:
                    ps_new |= {pn}
        ps = ps_new
    return(len(ps))

s = 0
for h in heads:
    s += find_trails(h)

print(s)
