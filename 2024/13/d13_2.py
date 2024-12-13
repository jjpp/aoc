#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def nums(l):
    d = l.split()
    if d[0] == 'Button':
        return int(d[2][2:-1]), int(d[3][2:])
    else:
        return int(d[1][2:-1]), int(d[2][2:])

t = 0

while len(ls) > 0:
    a = nums(ls.pop(0))
    b = nums(ls.pop(0))
    p = nums(ls.pop(0))
    while len(ls) > 0 and ls[0] == '':
        ls.pop(0)

    p = (p[0] + 10000000000000, p[1] + 10000000000000)

    #print(a, b, p)

    y = (p[1]*a[0] - p[0]*a[1]) / (b[1]*a[0] - b[0]*a[1])
    if y != int(y):
        #print("y = ", y, ": cannot win?")
        continue

    y = int(y)

    x = (p[0] - y*b[0]) / a[0]
    if x != int(x):
        #print("x = ", x, ": cannot win?")
        continue
    x = int(x)

    t += 3*int(x) + y

print(t)
