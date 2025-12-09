#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

N = len(ls)
for i in range(N):
    ls[i] = nums(ls[i])

maxa = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        area = (abs(ls[i][0] - ls[j][0]) + 1) * (abs(ls[i][1] - ls[j][1]) + 1)
        if area > maxa:
            maxa = area

print(maxa)

g = dict()
xs = list(sorted(set([l[0] for l in ls])))
ys = list(sorted(set([l[1] for l in ls])))

seen = set()

def tupleadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

# build the walls
for i in range(N):
    a = ls[i]
    b = ls[(i + 1) % N]
    a = (xs.index(a[0]), ys.index(a[1]))
    b = (xs.index(b[0]), ys.index(b[1]))
    g[a] = 1
    g[b] = 1
    d = (-1 if a[0] > b[0] else (1 if a[0] < b[0] else 0), -1 if a[1] > b[1] else (1 if a[1] < b[1] else 0))
    
    seen.add(b)
    while a != b:
        seen.add(a)
        g[a] = 1
        a = tupleadd(a, d)
        

s = { 0: 'X', -1: '.', 1: '#' }
q = [(-1, -1)]
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# fill outside of the wall with -1
while len(q) > 0:
    a = q.pop(0)
    if a in seen:
        continue
    g[a] = -1
    seen.add(a)

    for d in ds:
        b = tupleadd(a, d)
        if not b in seen and -2 <= b[0] <= len(xs)+2 and -2 <= b[1] <= len(ys) + 2:
            q.append(b)

#for j in range(len(ys) + 1):
#    print("" . join([s[g.get((i, j), 0)] for i in range(len(xs) + 1)]))
#print()



def checkarea(x1, y1, x2, y2):
    x1 = xs.index(x1)
    x2 = xs.index(x2)
    y1 = ys.index(y1)
    y2 = ys.index(y2)

    for i in range(min(x1, x2), max(x1, x2)+1):
        for j in range(min(y1, y2), max(y1, y2)+1):
            if (i, j) in g and g[i, j] == -1:
                return False

    return True

maxa = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        area = (abs(ls[i][0] - ls[j][0]) + 1) * (abs(ls[i][1] - ls[j][1]) + 1)
        if area > maxa:
            if not checkarea(ls[i][0], ls[i][1], ls[j][0], ls[j][1]):
                continue
            maxa = area

print(maxa)
