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

def range_minus(rs, r):
    out = []
    for ir in rs:
        if ir[1] < r[0] or ir[0] > r[1]:
            out.append(ir)
            continue
        if r[0] <= ir[0]:
            if ir[1] <= r[1]:
                continue
            out.append([r[1] + 1, ir[1]])
            continue

        out.append([ir[0], r[0] - 1])
        if r[1] < ir[1]:
            out.append([r[1] + 1, ir[1]])

    return(out)


def check_row(r, m):
    uncover = [[0, m]]
    for s in ss:
        if abs(s[1] - r) <= s[4]:
            d = s[4] - abs(s[1] - r)
            if s[0] + d < 0 or s[0] - d > m:
                continue
            uncover = range_minus(uncover, [max(s[0] - d, 0), min(s[0] + d, m)])

    if len(uncover) > 1:
        print(f"Should not be, r = {r}, |uc| = {len(uncover)}")
    elif len(uncover) == 1:
        if uncover[0][0] == uncover[0][1]:
            return uncover[0][0]
        else:
            print(f"Should not be: r = {r}, uc = {uncover}")
            return None
    else:
        return None


# for test input set this to M = 20:
M = 4000000
for r in range(0, M):
    c = check_row(r, M)
    if c != None:
        print(c * 4000000 + r)
        exit(0)

print("Should not reach here.")


