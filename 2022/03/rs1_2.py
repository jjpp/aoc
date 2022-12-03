#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

score = 0

for rs in ls:
    (f, s) = (rs[0:int(len(rs) / 2)], rs[int(len(rs) / 2):])
    i = list(set(f) & set(s))[0]
    if i.islower():
        score += ord(i) - ord('a') + 1
    else:
        score += ord(i) - ord('A') + 27

print(score)
