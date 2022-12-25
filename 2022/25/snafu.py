#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


s = 0
fs = '=-012'

for l in ls:
    v = 0
    for p in list(l):
        v *= 5
        v += fs.index(p) - 2
    s += v

out = ''
while s != 0:
    out = fs[(s + 2) % 5] + out
    s = (s + 2) // 5 

print(out)

