#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


c = 0
m = []
for l in ls:
    if l == "":
        m.append(c)
        c = 0
    else:
        c += int(l)

m.append(c)

m = list(reversed(sorted(m)))

print(m[0])
print(sum(m[0:3]))
        
