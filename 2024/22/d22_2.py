#!/usr/bin/python3

# part 2

import sys

ls = [int(l.strip()) for l in sys.stdin]

def step(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n

changes = {}

def steps(n, i):
    cs = []
    ccs = {}
    
    for _ in range(i):
        prev_n = n
        n = step(n)
        cs.append((n % 10) - (prev_n % 10))

        if len(cs) > 3:
            k = tuple(cs[-4:])
            if k not in ccs:
                ccs[k] = n % 10

    for k in ccs:
        if k not in changes:
            changes[k] = ccs[k]
        else:
            changes[k] += ccs[k]

for l in ls:
    steps(l, 2000)
       
print(max(changes.values()))
