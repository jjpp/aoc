#!/usr/bin/python3

# both parts, with comparator built for p2

import sys

ls = [l.strip() for l in sys.stdin]

rs = []
before = {}

while len(ls) > 0 and '|' in ls[0]:
    (x, y) = ls[0].split('|')
    rs.append((x, y))
    if x not in before:
        before[x] = set()
    before[x] |= {y}
    ls.pop(0)

if ls[0] == '':
    ls.pop(0)


class page(str):
    def __lt__(self, b):
        if self not in before:
            return False
        return b in before[self]

s1 = 0
s2 = 0
for l in ls:
    lls = l.split(',')
    lls_ = sorted([page(x) for x in lls])
    mid = int(lls_[int(len(lls) / 2)])
    if lls == lls_:
        s1 += mid
    else:
        s2 += mid

print(s1)
print(s2)

