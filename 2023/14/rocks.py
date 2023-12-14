#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)


def weight(r):
    l = 0
    s = 0
    for i in range(0, len(r)):
        if r[i] == '#':
            l = i + 1
        elif r[i] == 'O':
            s += len(r) - l 
            l += 1

    print(r, s)
    return s

print(sum([weight(r) for r in list(zip(*ls))]))


