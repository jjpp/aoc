#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

ns = {}
anti = set()

for j in range(Y):
    for i in range(X):
        p = i*(1j) + j
        l = ls[j][i]
        if l.isdigit() or l.isalpha():
            if l not in ns:
                ns[l] = set()
            ns[l] |= {p}

def in_grid(a):
    return a.imag >= 0 and a.imag < Y and a.real >= 0 and a.real < X


for l in ns:
    ps = list(ns[l])
    for i in range(len(ps) - 1):
        for j in range(i + 1, len(ps)):
            a, b = ps[i], ps[j]
            d = b - a

            a1 = a - d
            if in_grid(a1):
                anti |= {a1}

            a2 = b + d
            if in_grid(a2):
                anti |= {a2}

print(len(anti))
