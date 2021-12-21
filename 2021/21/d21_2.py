#!/usr/bin/python3

import sys
from itertools import product
from queue import PriorityQueue

(a, b) = [int(l.strip().split(' ')[4]) for l in sys.stdin]


print(a, b)

dist = {}
for d in product([1, 2, 3], repeat = 3):
    dist[sum(d)] = dist.get(sum(d), 0) + 1


w = 1
s = { (a, b, 0, 0, 0): 1 }

q = PriorityQueue()
q.put((0, (a, b, 0, 0, 0)))
inq = set([(a, b, 0, 0, 0)])

MAX = 21


while not q.empty():
    w *= 27
    (_, x) = q.get()
    inq.remove(x)
    print(f"checking {x} ({s[x]}), {q.qsize()}, {len(s)}")
    for r in dist:
        (a, b, ascore, bscore, p) = x
        a = ((a - 1) + r) % 10 + 1
        ascore += a
        outcomes = s[x] * dist[r]
        n = (b, a, bscore, ascore, 1 - p)
        # print(f"  new: ({r}, {dist[r]}) {n}")
        if not n in s:
            s[n] = outcomes
        else:
            s[n] = outcomes + s[n]

        if ascore < MAX and not n in inq:
            q.put((ascore + bscore, n))
            inq.add(n)

print(s)


wins = [0, 0]
for x in s:
    (a, b, ascore, bscore, p) = x
    if bscore >= MAX:
        print(f"{p} wins {s[x]} times in {x}")
        wins[p] += s[x]

print(wins)
print(max(wins))
    
