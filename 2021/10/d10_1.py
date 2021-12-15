#!/usr/bin/python3

import sys

match = { '(': ')', '[': ']', '<': '>', '{': '}' }
score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
score2 = { ')': 1, ']': 2, '}': 3, '>': 4 }

def check(w):
    s = []
    for c in w:
        if c in { '(', '[', '<', '{' }:
            s.append(match[c])
        else:
            if len(s) == 0 or s.pop() != c:
                return (score[c], 0)
    ls = 0
    while len(s) > 0:
        ls *= 5
        ls += score2[s.pop()]

    return (0, ls)

sum = 0
sum2 = []
for l in sys.stdin:
    l = l.strip()
    (s1, s2) = check(l)
    sum += s1
    if s2 > 0:
        sum2.append(s2)

win2 = sorted(sum2)[len(sum2)  // 2]
print(sum, win2)
