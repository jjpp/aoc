#!/usr/bin/python3

import sys
import functools

ls = [l.strip() for l in sys.stdin]
ls_ = [*ls]

ps = []

while len(ls) > 0:
    ps.append([eval(ls.pop(0)), eval(ls.pop(0))])
    if len(ls) > 0:
        ls.pop(0)

def cmp(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            c = cmp(a[i], b[i])
            if c > 0:
                return 1
            if c < 0:
                return -1
        if len(a) < len(b):
            return -1
        if len(a) > len(b):
            return 1
        return 0
    elif isinstance(a, list) and isinstance(b, int):
        return cmp(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return cmp([a], b)
    else:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

count = 0
for i in range(len(ps)):
    c = cmp(*ps[i])
    if c < 0 or (c == 0 and len(ps[i][0]) < len(ps[i][1])):
        count += 1 + i

print(count)


ps = [eval(l) for l in ls_ if l != '']
ps.append([[2]])
ps.append([[6]])

ps.sort(key = functools.cmp_to_key(cmp))

p = 1

for i in range(len(ps)):
    if ps[i] == [[2]] or ps[i] == [[6]]:
        p *= (i + 1)

print(p)

