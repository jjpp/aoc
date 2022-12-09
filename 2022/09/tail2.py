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
rope = [0, 0, 0, 0, 0,  0, 0, 0, 0, 0]
seent.add(0)

for c in ls:
    d = c[0]
    steps = int(c[1:])

    for s in range(0, steps):
        rd = dirs[d]
        rope[0] += dirs[d]
        old = [*rope]
        for i in range(0, len(rope) - 1):
            if abs(rope[i].real - rope[i + 1].real) > 1 and abs(rope[i].imag - rope[i + 1].imag) > 1:
                # must be diagonal movement
                rope[i + 1] += rd
            elif abs(rope[i].real - rope[i + 1].real) > 1:
                rope[i + 1] += rd
                if rope[i + 1].imag != rope[i].imag:
                    rope[i + 1] = complex(rope[i + 1].real, rope[i].imag)
            elif abs(rope[i].imag - rope[i + 1].imag) > 1:
                rope[i + 1] += rd
                if rope[i + 1].real != rope[i].real:
                    rope[i + 1] = complex(rope[i].real, rope[i + 1].imag)
            rd = rope[i + 1] - old[i + 1]

        seent.add(rope[9])

print(len(seent))



