#!/usr/bin/python3

# part 1 & 2, just lengths

import sys

ls = [l.strip() for l in sys.stdin]
ls = ls[0].split()

m = {}

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

def reciter(l, s):
    if s == 0:
        return 1

    if (l, s) in m:
        return m[l, s]

    n = iter([l])
    n = sum([reciter(n_, s - 1) for n_ in n])
    m[l, s] = n
    return n

print(sum([reciter(l, 25) for l in ls]))
print(sum([reciter(l, 75) for l in ls]))

