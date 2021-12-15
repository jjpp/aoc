#!/usr/bin/python3

import sys
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

cts = [int(s.strip()) for s in sys.stdin]

count = 0
minl = len(cts) + 1
minc = 0
for s in powerset(cts):
    if sum(s) == 150:
        count += 1
        if len(s) < minl:
            minl = len(s)
            minc = 1
        elif len(s) == minl:
            minc += 1


print(count, minc)
