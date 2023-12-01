#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

n = {
        'one': 1, 
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
}

for i in range(0, 10):
    n[str(i)] = i


def value(l):
    nrs = []
    for i in range(0, len(l)):
        for j in n.keys():
            if l[i:i+len(j)] == j:
                nrs.append(n[j])
    return 10*nrs[0] + nrs[-1]

print(sum([value(l) for l in ls]))

