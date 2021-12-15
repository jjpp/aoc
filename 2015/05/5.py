#!/usr/bin/python3

import sys

nice = 0
vowels = 'aeiou'

for w in sys.stdin:
    v = 1 if w[0] in vowels else 0
    same = 0
    naughty = 0
    for p in range(1, len(w) - 1):
        v += 1 if w[p] in vowels else 0
        pair = w[p - 1] + w[p]
        naughty += 1 if pair in ['ab', 'cd', 'pq', 'xy'] else 0
        same += 1 if pair[0] == pair[1] else 0
    nice += 1 if v > 2 and same > 0 and naughty == 0 else 0

print(nice)

