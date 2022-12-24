#!/usr/bin/python3

import sys
import math
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

g = {}
bs = []

bdirs = { '^': -1j, 'v': 1j, '<': -1, '>': 1 }
dirs = list(bdirs.values())

start = None
stop = None

R = len(ls)
C = len(ls[0])
period = (R - 2) * (C - 2) // math.gcd((R - 2), (C - 2))

for r in range(len(ls)):
    for c in range(len(ls[r])):
        p = complex(c, r)
        if ls[r][c] == '#':
            g[p] = '#'
        else:
            g[p] = '.'
            if r == 0:
                start = p
            if r == len(ls) - 1:
                stop = p

            if ls[r][c] in '<>v^':
                bs.append((p, bdirs[ls[r][c]]))

def bpos(p, d, s):
    p += d*s
    return complex((p.real - 1) % (C - 2) + 1, (p.imag - 1) % (R - 2) + 1)

bps_ = [set([bpos(p, d, i) for (p, d) in bs]) for i in range(period)]

def solve(start, stop, initial_step):
    q = PriorityQueue()
    q.put((initial_step, start.real, start.imag))
    dist = {}
    dist[start, initial_step % period] = 0
    seen = set()

    while not q.empty() and stop not in dist:
        (step, x, y) = q.get()

        if (step, x, y) in seen:
            continue

        seen.add((step, x, y))
        pos = complex(x, y)

        bps = bps_[(step + 1) % period]

        for d in dirs + [0]:
            np = pos + d

            if np in g and g[np] == '.' and np not in bps:
                if np == stop:
                    return step + 1
                if (np, (step + 1) % period) not in dist or dist[np, (step + 1) % period] > dist[pos, step % period]:
                    dist[np, (step + 1) % period] = step + 1
                    q.put((step + 1, np.real, np.imag))

there = solve(start, stop, 0)
back = solve(stop, start, there)
there_again = solve(start, stop, back)

print(there)
print(there_again)


