#!/usr/bin/python3

# part 2

import sys

ls = [l.strip() for l in sys.stdin]


N = '789456123 0A'
D = ' ^A<v>'

m = {}
s = 0


def step(kp, a, b, depth):
    if (kp, a, b, depth) in m:
        return m[kp, a, b, depth]

    pa = kp.index(a)
    pb = kp.index(b)
    dx = pb % 3 - pa % 3
    dy = (pb // 3) - (pa // 3)


    if depth == 0:
        return abs(dx) + abs(dy) + 1

    cx = cy = ""

    if dy < 0:
        cy = '^' * abs(dy)
    else:
        cy = 'v' * abs(dy)

    if dx < 0:
        cx = '<' * abs(dx)
    else:
        cx = '>' * abs(dx)

    hf = [] if kp[pa + dx] == ' '   else [minlen(D, cx + cy + 'A', depth - 1)]
    vf = [] if kp[pa + 3*dy] == ' ' else [minlen(D, cy + cx + 'A', depth - 1)]

    m[kp, a, b, depth] = min(hf + vf)
    return m[kp, a, b, depth]
    

def minlen(kp, code, depth):
    pairs = zip('A' + code[:-1], code)
    return sum([step(kp, a, b, depth) for (a, b) in pairs])

DEPTH = 25
for l in ls:
    ml = minlen(N, l, DEPTH)
    cs = int(l[0:3]) * ml
    s += cs
    # print(s, cs, int(l[0:3]), ml)

print(s)
