#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)
been = set()
been2 = set()
obst = set()

d = -1j + 0
for j in range(0, Y):
    if '^' in ls[j]:
        p = j*(1j) + ls[j].index('^')
        break
initial_p = p

def print_m(p, d, o = None, been = None):
    ds = {
        (-1j): '^',
        (1j): 'v',
        (1): '>',
        (-1): '<'
    }
    b = {p[0] for p in been}
    for j in range(0, Y):
        out = ""
        for i in range(0, X):
            p_ = j*(1j) + i
            if p == p_:
                out += ds[d]
            elif p == o:
                out += 'O'
            else:
                if p_ in b:
                    out += 'X'
                else:
                    out += ls[j][i]
        print(out)
    print(len(been), d, p)
    print()

def would_loop(o, p, d):
    been_ = { *been }
    d = d * 1j

    while True:
        if (p, d) in been_:
            return True

        been_ |= {(p, d)}

        n_ = p + d
        if n_.imag < 0 or int(n_.imag) >= Y or n_.real < 0 or int(n_.real) >= X:
            return False

        if ls[int(n_.imag)][int(n_.real)] == '#' or n_ == o:
            d = d * 1j
            continue

        p = n_
    

while True:
    been |= {(p, d)}
    been2 |= {p}
    # print_m(p, d)
    n = p + d
    if n.imag < 0 or int(n.imag) >= Y or n.real < 0 or int(n.real) >= X:
        break

    if ls[int(n.imag)][int(n.real)] == '#':
        d = d * (1j)
        continue

    if n != initial_p and (n not in been2) and would_loop(n, p, d):
        obst |= {n}

    p = n


print(len(obst))

