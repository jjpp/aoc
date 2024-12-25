#!/usr/bin/python3

import sys, re
from itertools import product

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

keys = []
locks = []

i = 0
j = 0
while i < len(ls):
    if '#' in ls[i]:
        key = []
        for j in range(len(ls[i])):
            c = [ls[i + k][j] for k in range(7)]
            key.append(c.index('.') - 1)
        keys.append(key)
    elif '.' in ls[i]:
        lock = []
        for j in range(len(ls[i])):
            c = [ls[i + k][j] for k in range(7)]
            lock.append(6 - c.index('#'))
        locks.append(lock)
    i += 8

s = 0 
for (k, l) in product(keys, locks):
    if all([k[i] + l[i] < 6 for i in range(5)]):
        s += 1

print(s)
