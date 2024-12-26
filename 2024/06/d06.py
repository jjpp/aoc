#!/usr/bin/python3

# part 1

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)
been = set()

d = -1j + 0
for j in range(0, Y):
    if '^' in ls[j]:
        p = j*(1j) + ls[j].index('^')
        break

def print_m(p, d):
    ds = {
        (-1j): '^',
        (1j): 'v',
        (1): '>',
        (-1): '<'
    }
    for j in range(0, Y):
        out = ""
        for i in range(0, X):
            p_ = j*(1j) + i
            if p == p_:
                out += ds[d]
            else:
                if p_ in been:
                    out += 'X'
                else:
                    out += ls[j][i]
        print(out)
    print(len(been), d, p)
    print()

while True:
    been |= {p}
    # print_m(p, d)
    n = p + d
    if n.imag < 0 or int(n.imag) >= Y or n.real < 0 or int(n.real) >= X:
        break

    if ls[int(n.imag)][int(n.real)] == '#':
        d = d * (1j)
        continue

    p = n

print(len(been))

