#!/usr/bin/python3

# part 1

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

c = 0

for j in range(0, Y):
    for i in range(0, X):
        if i <= X - 4:
            test = ls[j][i:i+4]
            if test == 'XMAS':
                c += 1
            if test == 'SAMX':
                c += 1
        if j <= Y - 4:
            test = "".join([ls[j + j_][i] for j_ in range(0, 4)])
            if test == 'XMAS':
                c += 1
            if test == 'SAMX':
                c += 1
        if i <= X - 4 and j >= 3:
            test = "".join([ls[j - j_][i + j_] for j_ in range(0, 4)])
            if test == 'XMAS':
                c += 1
            if test == 'SAMX':
                c += 1

        if i <= X - 4 and j <= Y - 4:
            test = "".join([ls[j + j_][i + j_] for j_ in range(0, 4)])
            if test == 'XMAS':
                c += 1
            if test == 'SAMX':
                c += 1

print(c)

