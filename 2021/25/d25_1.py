#!/usr/bin/python3

import sys

lns = [l.strip() for l in sys.stdin]

g = {}

for r, l in enumerate(lns):
    for c, p in enumerate(l):
        g[c, r] = p

X = len(lns[0])
Y = len(lns)


def step(g):
    o = g.copy()

    for y in range(Y):
        for x in range(X):
            if g[x, y] == '>':
                if g[(x + 1) % X, y] == '.':
                    o[(x + 1) % X, y] = '>'
                    o[x, y] = '.'
    #global count
    #print(f"\nAt step {count + 1} first")
    #for y in range(Y):
    #    print("".join([o[x, y] for x in range(X)]))
    g = o.copy()

    for y in range(Y):
        for x in range(X):
            if g[x, y] == 'v':
                if g[x, (y + 1) % Y] == '.':
                    o[x, (y + 1) % Y] = 'v'
                    o[x, y] = '.'

    #print(f"\nAt step {count + 1} second")
    #for y in range(Y):
    #    print("".join([o[x, y] for x in range(X)]))

    return o

#for y in range(Y):
#    print("".join([g[x, y] for x in range(X)]))


count = 0
while True:
    old_g = g.copy()
    g = step(g)
    count += 1
    if old_g == g:
        break

print(count)

