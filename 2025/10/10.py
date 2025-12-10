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

def push(t, b):
    nt = [*t]
    for p in b:
        if nt[p] == 0:
            return None
        nt[p] -= 1
    return nt

def all_zero(t):
    return all([x == 0 for x in t])

bl = {}
def can(t, bs):
    if len(bs) not in bl:
        bits = set()
        for b in bs:
            bits |= set(b)
        bl[len(bs)] = bits

    bits = bl[len(bs)]
    return not any([t[i] > 0 for i in range(len(t)) if i not in bits])

def tries2(t, bs, pushed):
    if all_zero(t):
        return pushed
    if len(bs) == 0 or not can(t, bs):
        return 9999999999

#    print(t, bs, pushed)

    mp = tries2(t, bs[1:], pushed)
    nt = push(t, bs[0])
    c = 1
    while nt != None:
        mp = min(mp, tries2(nt, bs[1:], pushed + c))
        c += 1
        nt = push(nt, bs[0])

    return mp

seen = {}


def tries3(t, bs, pushed, p):
    if p == len(t):
        return pushed

    if t[p] == 0:
        return tries3(t, bs, pushed, p + 1)

    # print("t3", t, bs, pushed, p)

    key = str(t) + str(bs)
    if key in seen:
        # print("seen:", key)
        (dist, left) = seen[key]
        if (dist > pushed):
            seen[key] = (pushed, left)
            dist = pushed
        return dist + left

    mp = 99999999
    for b in bs:
        if p not in b:
            continue
        bn = [*bs]
        bn.remove(b)
        nt = [*t]
        c = 0
        while nt != None:
            mp = min(mp, tries3(nt, bn, pushed + c, p))
            c += 1
            nt = push(nt, b)

    seen[key] = (pushed, mp - pushed)
    return mp



def bfs(t, bs):
    queue = PriorityQueue()
    dist = {}
    dist[str(t)] = 0

    queue.put((max(t), 0, t, sum(t), 0))
    mind = 99999999999
    steps = 0
    maxage = 0
    while not queue.empty():
        (z, d, tt, s, it) = queue.get()
        steps += 1

#        print(z, d, s, tt, len(dist))

        if s == 0:
            mind = min(mind, d)
            print("mind = ", mind, steps)
            return mind

        if d >= mind:
            continue

        k = str(tt)
        if dist[k] < d:
            continue

        maxage = max(maxage, steps - it)

        if (steps % 100000) == 0:
            print(z, d, tt, s, len(dist), queue.qsize(), it, maxage)
        

        for b in bs:
            nt = push(tt, b)
            if nt != None:
                kk = str(nt)
                if kk in dist and dist[kk] <= d:
                    continue

                tpl = (max(nt), d + 1, nt, sum(nt), steps)

                if (kk not in dist or dist[kk] > d + 1):
                    if kk in dist:
                        print("shorter way:", tt, " -> ", nt, b, dist[kk], d + 1)
                    dist[kk] = d + 1
                    queue.put(tpl)

    return mind

def tries4(t, bs):
    q = PriorityQueue()
    nq = PriorityQueue()
    dist = {}
    dist[str(t)] = 0
    q.put(((0, 0), t, 0))
    wq = None
    
    def fill(t, d, p, bs):
        if len(bs) == 0:
            return

        if t[p] == 0:
            q.put(((0, sum(t)), t, d))
            return

        fill(t, d, p, bs[1:])
        if p not in bs[0]:
            return

        #print("fill: ", t, d, p, bs)

        #if any([t[i] > 0 for i in range(p)]):
        #    print("fill ", p, " but ", t)

        nt = push(t, bs[0])
        if nt == None:
            return

        k = str(nt)
        if k not in dist or dist[k] > d + 1:
            dist[k] = d + 1
            tpl = ((nt[p], sum(nt)), nt, d + 1)
            if nt[p] == 0:
                #print("adding ", tpl)
                q.put(tpl)
            else:
                wq.put(tpl)


    cs = Counter()
    for b in bs:
        cs.update(b)

    keys = [(t[i] ** c, i) for (i, c) in cs.most_common()]

    for (c, i) in sorted(keys):
        wq = q
        q = nq
        nq = PriorityQueue()

        print("pos ", i, c, wq.qsize())

        sts = 0

        subbs = [b for b in bs if i in b]
        if len(subbs) == 0:
            q = wq
            print("no subbs?")
            continue

        while not wq.empty():
            (z, ot, d) = wq.get()
            #print(ot, d)
            if dist[str(ot)] < d:
                continue
            if sum(ot) == 0:
                return d

            sts += 1
            if (sts % 1000000) == 0:
                print("step", sts, i, wq.qsize(), q.qsize(), len(dist), ot, t[i], len(subbs))

            fill(ot, d, i, subbs)

        print("after pos ", i, q.qsize())

    (ot, d) = q.get()
    if sum(ot) != 0:
        print("???", sum(ot), ot, q.qsize())
    return d



def tries5(t, bs):
    print(t)
    q = PriorityQueue()
    nq = PriorityQueue()
    dist = {}
    dist[str(t)] = 0
    q.put(((0, 0), t, 0))
    wq = None
    
    def fill(t, d, p, bs):
        if len(bs) == 0:
            return

        if t[p] == 0:
            q.put(((0, sum(t)), t, d))
            return

        fill(t, d, p, bs[1:])
        #if p not in bs[0]:
        #    return

        #print("fill: ", t, d, p, bs)

        #if any([t[i] > 0 for i in range(p)]):
        #    print("fill ", p, " but ", t)

        nt = push(t, bs[0])
        c = d + 1
        while nt != None:
            k = str(nt)
            if k not in dist or dist[k] > c:
                dist[k] = c
                tpl = ((nt[p], sum(nt)), nt, c)
                if nt[p] == 0:
                    #print("adding ", tpl)
                    q.put(tpl)
                else:
                    wq.put(tpl)
            nt = push(nt, bs[0])
            c += 1


    cs = Counter()
    for b in bs:
        cs.update(b)
    print(cs.most_common())

    pi = [ sum([len(b) for b in bs if i in b]) for i in range(len(t)) ]
    print(pi)

    keys = [(c * t[i] * pi[i], i) for (i, c) in cs.most_common()]

    for (c, i) in sorted(keys):
        wq = q
        q = nq
        nq = PriorityQueue()

        print("pos ", i, c, wq.qsize())

        sts = 0

        subbs = [b for b in bs if i in b]
        if len(subbs) == 0:
            q = wq
            print("no subbs?")
            continue

        while not wq.empty():
            (z, ot, d) = wq.get()
            #print(ot, d)
            if dist[str(ot)] < d:
                continue
            if sum(ot) == 0:
                return d

            sts += 1
            if (sts % 1000000) == 0:
                print("step", sts, i, wq.qsize(), q.qsize(), len(dist), ot, t[i], len(subbs))

            fill(ot, d, i, subbs)

        print("after pos ", i, q.qsize(), sts)

    (z, ot, d) = q.get()
    if sum(ot) != 0:
        print("???", sum(ot), ot, q.qsize())
    print(d)
    return d


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
