#!/usr/bin/python3

import sys

ls = [int(l.strip()) for l in sys.stdin]
ls2 = [i * 811589153 for i in ls]
order = list(range(len(ls)))

for p in range(len(ls)):
    i = order.index(p)
    x = ls[i]
    ni = (len(ls) - 1 + x + i) % (len(ls) - 1)

    if ni < i:
        ls =    [   *ls[:ni], x,    *ls[ni:i],    *ls[i+1:]]
        order = [*order[:ni], p, *order[ni:i], *order[i+1:]]
    else:
        ls =    [   *ls[:i],    *ls[i+1:ni+1], x,    *ls[ni+1:]]
        order = [*order[:i], *order[i+1:ni+1], p, *order[ni+1:]]



z = ls.index(0)

print(ls[(z + 1000) % len(ls)] + ls[(z + 2000) % len(ls)] + ls[(z + 3000) % len(ls)])

ls = ls2
order = list(range(len(ls)))

for _ in range(10):
    for p in range(len(ls)):
        i = order.index(p)
        x = ls[i]
        ni = (len(ls) - 1 + x + i) % (len(ls) - 1)

        if ni < i:
            ls =    [   *ls[:ni], x,    *ls[ni:i],    *ls[i+1:]]
            order = [*order[:ni], p, *order[ni:i], *order[i+1:]]
        else:
            ls =    [   *ls[:i],    *ls[i+1:ni+1], x,    *ls[ni+1:]]
            order = [*order[:i], *order[i+1:ni+1], p, *order[ni+1:]]

z = ls.index(0)
print(ls[(z + 1000) % len(ls)] + ls[(z + 2000) % len(ls)] + ls[(z + 3000) % len(ls)])
