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

def find_rating(p):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ps = {p}
    trails = dict()
    trails[p] = [p]
    count_trails = 0
    for step in range(1, 10):
        s_ = str(step)
        ps_new = set()
        for p_ in ps:
            for d in dirs:
                pn = (p_[0] + d[0], p_[1] + d[1])
                if in_grid(*pn) and ls[pn[1]][pn[0]] == s_:
                    ps_new |= {pn}
                    if pn not in trails:
                        trails[pn] = set()
                    trails[pn] |= set([ tuple([*t, pn]) for t in trails[p_] ])

        ps = ps_new
    
    return sum([len(t) for (p, t) in trails.items() if ls[p[1]][p[0]] == '9'])

s = 0
for h in heads:
    s += find_rating(h)

print(s)
