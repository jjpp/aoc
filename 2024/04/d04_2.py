#!/usr/bin/python3

# part 2

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

c = 0

for j in range(0, Y - 2):
    for i in range(0, X - 2):
        t1 = "".join([ls[j + j_][i+j_] for j_ in range(0, 3)])
        t2 = "".join([ls[j + 2 - j_][i+j_] for j_ in range(0, 3)])

        if (t1 in ['MAS', 'SAM']) and (t2 in ['MAS', 'SAM']):
            c += 1

print(c)

