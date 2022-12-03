#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

score = 0

while len(ls) > 0:
    seen = {}
    for z in range(0, 3):
        s = ls.pop(0)
        xls = {}
        for c in s:
            if c in xls:
                continue
            xls[c] = True
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1

    c = [c for c in seen if seen[c] == 3][0]

    if c <= 'Z':
        score += ord(c) - ord('A') + 27
    else:
        score += ord(c) - ord('a') + 1

print(score)
