#!/usr/bin/python3

import sys
from math import prod

ls = [l.strip() for l in sys.stdin]

n = []
a = []

for l in ls:
    d = l.split()
    n.append(int(d[3]))
    a.append(int(d[11][:-1]))

n.append(11)
a.append(0)

def check(x):
    for i in range(0, len(n)):
        if (x + 1 + i + a[i]) % n[i] != 0:
            return False
    return True

for x in range(0, prod(n)):
    if check(x):
        print(x)
        break


