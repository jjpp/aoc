#!/usr/bin/python3

import sys
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)
sy = min([i for i in range(0, Y) if 'S' in ls[i]])
sx = ls[sy].index('S')

d = {}
q = PriorityQueue()

ds = ((1, 0), (-1, 0), (0, 1), (0, -1))

q.put((0, (sx, sy)))


step = 0
ss = []

def print_map():
    print("Map for step count", step)
    for y in range(-Y, 2*Y):
        o = ""
        for x in range(-X, 2*X):
            if (x, y, step % 2) in d and d[x, y, step % 2] <= step:
                o += "O"
            else:
                o += ls[(y % Y + Y) % Y][(x % X + X) % X]
        print(o)
    print()

def print_submaps(q_):
    for y_ in range(-q_, q_):
        out = ""
        for x_ in range(-q_, q_):
            out += "%6d" % (sum([1 if (x + x_ * X, y + y_ * Y, step % 2) in d else 0 for x in range(0, X) for y in range(0, Y)]))
        print(out)

#      0     0     0     0     0     0
#      0     0   937  5544   930     0
#      0   937  6453  7410  6454   930
#      0  5553  7410  7363  7410  5540
#      0   949  6463  7410  6449   954
#      0     0   949  5549   954     0


maps = [
        (0, 0, lambda n: (n - 1) * (n - 1)),
        (1, 0, lambda n: (n * n)),
        (-2, 0, lambda n: 1),
        (2, 0, lambda n: 1),
        (0, -2, lambda n: 1),
        (0, 2, lambda n: 1),
        (-1, -2, lambda n: n),
        (1, -2, lambda n: n),
        (-1, 2, lambda n: n),
        (1, 2, lambda n: n),
        (-1, -1, lambda n: n - 1),
        (-1, 1, lambda n: n - 1),
        (1, -1, lambda n: n - 1),
        (1, 1, lambda n: n - 1),
]

steps_to_go = 26501365

HALF = int((X - 1) / 2)
ONE = X
TWO = 2 * ONE

while not q.empty():
    (dist, (x, y)) = q.get()
    if ls[(y + Y) % Y][(x + X) % X] == '#':
        continue

    if dist > step:
        # when ever we have completed a step (there is a new dist)
        if step >= (HALF + TWO) and (step - HALF) % TWO == 0:
            # print(step, sum([1 if d[(x, y, dist)] <= step and dist % 2 == step % 2 else 0 for (x, y, dist) in d]))
            n = int((steps_to_go - HALF) / ONE)
            s_ = 0

            # print_submaps(3)

            for mp in maps:
                mult = mp[2](n)
                s_ += sum([mult if (x + mp[0] * X, y + mp[1] * Y, step % 2) in d else 0 for x in range(0, X) for y in range(0, Y)])
            print(s_)

            exit(0)

        #print_map()
        step = dist

    if (x, y, dist % 2) in d:
        continue

    d[x, y, dist % 2] = dist

    for d_ in ds:
        q.put((dist + 1, (x + d_[0], y + d_[1])))

print("Should not reach here.")
