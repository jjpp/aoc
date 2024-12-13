#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

counted = {}
total = 0
blobs = 0
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_grid(x, y):
    return 0 <= x < X and 0 <= y < Y

def count(i, j):
    global blobs
    global total
    q = [(i, j)]
    c = ls[j][i]
    blob = blobs
    blobs += 1
    area = 0
    perimeter = 0
    while len(q) > 0:
        (x, y) = q.pop()
        if not in_grid(x, y):
            continue
        if ls[y][x] != c or (x, y) in counted:
            continue
        for d in ds:
            q.append((x + d[0], y + d[1]))
        area += 1
        counted[(x, y)] = blob

    for y in range(Y):
        for x in range(X):
            if counted.get((x, y), None) == blob:
                for d in ds:
                    (x_, y_) = (x + d[0], y + d[1])
                    if not in_grid(x_, y_) or counted.get((x_, y_), None) != blob:
                        perimeter += 1

    print("Found ", c, " with area ", area, perimeter)
    total += area*perimeter



for j in range(Y):
    for i in range(X):
        if (i, j) not in counted:
            count(i, j)

print(total)


