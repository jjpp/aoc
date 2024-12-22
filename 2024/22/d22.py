#!/usr/bin/python3

import sys

ls = [int(l.strip()) for l in sys.stdin]

def step(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n

def steps(n, i):
    for _ in range(i):
        n = step(n)
    return n


s = 0
print(sum([steps(n, 2000) for n in ls]))

