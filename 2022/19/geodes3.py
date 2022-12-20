#!/usr/bin/python3

import sys
import re
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]


bps = []

for l in ls:
    ns = list(map(int, re.findall("\d+", l)))

    bps.append([ns[0], [(0, -ns[6], 0, -ns[5]), (0, 0, -ns[4], -ns[3]), (0, 0, 0, -ns[2]), (0, 0, 0, -ns[1])]])


def tadd(t, i, v):
    l = list(t)
    l[i] += v
    return tuple(l)

def tplus(t, u):
    return tuple(map(sum, zip(t, u)))

def tbigger(t, u):
    return min(map(sum, zip(t, u))) >= 0

best = 0
def solve_bp(bp, S = 32):
    global best
    conf = {}
    best = 0
    max_use = tuple(map(min, zip(*bp[1])))

    print(bp, max_use)
    q = PriorityQueue()

    def add(t, r, b):
        if t > S:
            return
#        print("adding", t, r, b)
        k = tuple([-i for i in [*b, *r, t]])
        q.put((k, (t, r, b)))

    def step(t, r, b):
        global best
        if t > S:
            return

        key = (t, b, tuple(r[3:4]))
        v = tuple([*r, *b])
        if key not in conf or conf[key] < v:
            conf[key] = v
            if r[0] > best:
                print(r[0], t, r, b)
            best = max(best, r[0])
        else:
            return

#        print("checking", t, r, b)

        r_ = tplus(r, b)

        # can create geode bot
        if tbigger(r, bp[1][0]):
            add(t + 1, tplus(r_, bp[1][0]), tadd(b, 0, 1))
            return

        add(t + 1, r_, b)

        for ri in range(1, 4):
            if b[ri] <= -max_use[ri] and tbigger(r, bp[1][ri]):
                add(t + 1, tplus(r_, bp[1][ri]), tadd(b, ri, 1))

    add(0, (0, 0, 0, 0), (0, 0, 0, 1))
    while not q.empty():
        (_k, (t, r, b)) = q.get()
        step(t, r, b)


    print("Blueprint ", bp[0], best)

    return best

print(solve_bp(bps[0]) * solve_bp(bps[1]) * solve_bp(bps[2]))




