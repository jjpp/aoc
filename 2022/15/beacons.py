#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ss = []
bs = {}

for l in ls:
    ps = l.split(' ')
    x = int(ps[2][2:-1])
    y = int(ps[3][2:-1])
    sx = int(ps[8][2:-1])
    sy = int(ps[9][2:])

    ss.append([x, y, sx, sy, abs(sx - x) + abs(sy - y)])
    bs[complex(sx, sy)] = True
    bs[complex(x, y)] = True

def check_row(r):
    cover = set()
    for s in ss:
        if abs(s[1] - r) <= s[4]:
            for c in range(s[0] - s[4] - 1, s[0] + s[4] + 2):
                if (abs(s[0] - c) + abs(s[1] - r)) <= s[4]:
                    if complex(c, r) not in bs:
                        cover.add(c)

    return len(cover)

#print(check_row(10))
print(check_row(2000000))



