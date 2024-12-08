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

steps = max(X, Y)

for l in ns:
    ps = list(ns[l])
    for i in range(len(ps) - 1):
        for j in range(i + 1, len(ps)):
            ii, ij = int(ps[i].imag), int(ps[i].real)
            ji, jj = int(ps[j].imag), int(ps[j].real)
            di = ji - ii
            dj = jj - ij

            for s in range(-steps, steps + 1):
                a1 = (ii - s * di) + 1j*(ij - s * dj)
                if a1.imag >= 0 and a1.imag < Y and a1.real >= 0 and a1.real < X:
                    anti |= {a1}

print(len(anti))
