#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

dirs = {
        'R': 1,
        'L': -1,
        'U': 1j,
        'D': -1j,
}

seent = set()
h = t = 0
seent.add(0)

for c in ls:
    d = c[0]
    steps = int(c[1:])

    for s in range(0, steps):
        h += dirs[d]
        if abs(h.real - t.real) > 1:
            t += dirs[d]
            if t.imag != h.imag:
                t = complex(t.real, h.imag)
        elif abs(h.imag - t.imag) > 1:
            t += dirs[d]
            if t.real != h.real:
                t = complex(h.real, t.imag)

        seent.add(t)

print(len(seent))



