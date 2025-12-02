#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("\\d+", l)))

ns = nums(ls[0])

def isinvalid(i):
    s = str(i)
    l = len(s)
    return (l % 2 == 0) and s[0:int(l/2)] == s[int(l/2):]

def isinvalid2(i):
    s = str(i)
    l = len(s)
    for j in range(1, int(l/2) + 1):
        if s[0:j] * int(l/j) == s:
            return True
    return False

s = 0
s2 = 0
while len(ns) > 0:
    (a, b) = (ns.pop(0), ns.pop(0))

    for i in range(a, b+1):
        if isinvalid(i):
            s += i
        if isinvalid2(i):
            s2 += i

print(s)
print(s2)
