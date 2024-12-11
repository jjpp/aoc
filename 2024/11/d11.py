#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]
ls = ls[0].split()

def iter(ls):
    n = []
    for l in ls:
        if l == '0':
            n.append('1')
        elif len(l) % 2 == 0:
            n.append(l[0:int(len(l)/2)])
            n.append(str(int(l[int(len(l)/2):])))
        else:
            n.append(str(int(l) * 2024))

    return n

for _ in range(25):
    ls = iter(ls)

print(len(ls))

for _ in range(50):
    ls = iter(ls)

print(len(ls))
