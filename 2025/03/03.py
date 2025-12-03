#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

s = 0
s12 = 0

for l in ls:
    ss = l[0:2]
    for i in range(2, len(l)):
        ss = max(ss, max(ss[0] + l[i], ss[1] + l[i]))
    s += int(ss)
    
for l in ls:
    ss = l[0:12]
    for i in range(12, len(l)):
        st = ss
        for j in range(0, 12):
            st = max(st, ss[0:j] + ss[j + 1:] + l[i])
        ss = max(ss, st)

    s12 += int(ss)


print(s)
print(s12)
