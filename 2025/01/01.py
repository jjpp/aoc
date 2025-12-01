#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

c = 50
count = 0
clicks = 0

for l in ls:
    coeff = 1 if l[0] == 'R' else -1
    steps = nums(l)[0]

    while steps > 0:
        c += 100 + coeff
        c %= 100
        steps -= 1
        if c == 0:
            clicks += 1

    if c == 0:
        count += 1

#    print(l, c, count, clicks)

print(count)
print(clicks)
