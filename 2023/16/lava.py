#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)


def count(x__, y__, dx__, dy__):
    b = {}

    check = []
    check.append((x__, y__, dx__, dy__))

    while len(check) > 0:
        (x, y, dx, dy) = check.pop()

        if (x, y) != (x__, y__):
            if (x, y) not in b:
                b[x, y] = {}
            if (dx, dy) in b[x, y]:
                continue
            b[x, y][dx, dy] = True

        x_ = x + dx
        y_ = y + dy
        if x_ < 0 or y_ < 0 or x_ >= X or y_ >= Y:
            continue

        if ls[y_][x_] == '.':
            check.append((x_, y_, dx, dy))
        elif ls[y_][x_] == '\\':
            check.append((x_, y_, dy, dx))
        elif ls[y_][x_] == '/':
            check.append((x_, y_, -dy, -dx))
        elif ls[y_][x_] == '|':
            if dx == 0:
                check.append((x_, y_, dx, dy))
            else:
                check.append((x_, y_, 0, 1))
                check.append((x_, y_, 0, -1))
        elif ls[y_][x_] == '-':
            if dx != 0:
                check.append((x_, y_, dx, dy))
            else:
                check.append((x_, y_, 1, 0))
                check.append((x_, y_, -1, 0))

    return len(b.keys())

print(count(-1, 0, 1, 0))

m = 0

for i in range(0, X):
    m = max(m, count(i, -1, 0, 1))
    m = max(m, count(i, Y, 0, -1))

for j in range(0, Y):
    m = max(m, count(-1, i, 1, 0))
    m = max(m, count(X, i, -1, 0))

print(m)

