#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


out1 = []

cmd = {
        'U': [0,   0, -2,  0,   0, -4, -4, -4,  0,   -4, -4, -4,   -2],
        'D': [2,   4,  4,  4,   0,  4,  4,  4,  0,    0,  2,  0,    0],
        'L': [0,   0, -1, -1,   0, -1, -1, -1, -1,    0, -1, -1,    0],
        'R': [0,   1,  1,  0,   1,  1,  1,  1,  0,    1,  1,  0,    0],
}

s = '123456789ABCD'

n1 = 4

for l in ls:
    print(l)
    for c in l:
        n1 += cmd[c][n1]
        print(n1 + 1)

    out1.append(s[n1])

print("".join(out1))

