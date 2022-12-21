#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]


m = {}

for l in ls:
    n, v = l.split(': ')
    d = v.split(' ')
    if len(d) == 1:
        m[n] = v
    else:
        m[n] = d

while not isinstance(m['root'], str):
    for k in m:
        if isinstance(m[k], list):
            if not(isinstance(m[m[k][0]], list)) and not(isinstance(m[m[k][2]], list)):
                m[k] = str(int(eval(m[m[k][0]] + m[k][1] + m[m[k][2]])))

print(m['root'])

