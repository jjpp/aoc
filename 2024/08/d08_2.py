#!/usr/bin/python3

# part 2

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

steps = max(X, Y)

for l in ns:
    ps = list(ns[l])
    for i in range(len(ps) - 1):
        for j in range(i + 1, len(ps)):
            a, b = ps[i], ps[j]
            d = b - a

            for s in range(-steps, steps + 1):
                a1 = a + s*d
                if in_grid(a1):
                    anti |= {a1}

print(len(anti))

