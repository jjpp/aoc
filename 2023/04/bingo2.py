#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

copies = []

def value(l):
    global copies
    c = l.split()
    #i = int(c[1])
    bar = c.index('|')
    winning = c[2:bar]
    yours = c[bar:]
    points = [w for w in winning if w in yours]
    extra = copies.pop(0) if len(copies) > 0 else 0
    for i in range(0, len(points)):
        if i < len(copies):
            copies[i] += (1 + extra)
        else:
            copies.append(1 + extra)

    # print(f"{c[1]} {1 + extra} copies, copies = {copies}")
    return 1 + extra

print(sum([value(l) for l in ls]))

