#!/usr/bin/python3

# part 2, original

import sys

ls = [l.strip() for l in sys.stdin]

rs = []
before = {}

while len(ls) > 0 and '|' in ls[0]:
    (x, y) = ls[0].split('|')
    x = int(x)
    y = int(y)
    rs.append((x, y))
    if x not in before:
        before[x] = set()
    before[x] |= {y}
    ls.pop(0)

if ls[0] == '':
    ls.pop(0)

def in_order(xs):
    for i in range(len(xs)):
        if i > 0 and not all([xs[i] in before[x] for x in xs[0:i] if x in before]):
            return False
        if i > 0 and any([x in before[xs[i]] for x in xs[0:i] if xs[i] in before]):
            return False
        if i < len(xs) - 1 and not all([x in before[xs[i]] for x in xs[i+1:] if xs[i] in before]):
            return False
        if i < len(xs) - 1 and any([xs[i] in before[x] for x in xs[i+1:] if x in before]):
            return False
    return True

class page(int):
    def __lt__(self, b):
        if self not in before:
            return False
        return b in before[self]

s = 0
for l in ls:
    lls = [int(x) for x in l.split(',')]
    if not in_order(lls):
        lls = sorted([page(x) for x in lls])
        s += lls[int(len(lls) / 2)]

print(s)

