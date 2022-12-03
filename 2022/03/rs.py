#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

score = 0

for rs in ls:
    (f, s) = (rs[0:int(len(rs) / 2)], rs[int(len(rs) / 2):])
    seen = {}
    for i in f:
        if i in s and not i in seen:
            seen[i] = True
            if i.islower():
                score += ord(i) - ord('a') + 1
            else:
                score += ord(i) - ord('A') + 27

print(score)
