#!/usr/bin/python3

# part 1 & 2

import sys

ls = [l.strip() for l in sys.stdin]

X = len(ls[0])
Y = len(ls)

counted = {}
total = 0
total2 = 0
blobs = 0
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_grid(x, y):
    return 0 <= x < X and 0 <= y < Y

def count(i, j):
    global blobs
    global total, total2
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
    sv = [False] * (X + 1)
    sides = 0

    for y in range(Y + 1):
        sh = False
        for x in range(X + 1):
            #print(" checking", x, y, sv, sh)
            if in_grid(x, y) and counted.get((x, y), None) == blob:
                (x_, y_) = (x - 1, y)
                if not in_grid(x_, y_) or counted.get((x_, y_), None) != blob:
                    if not sv[x] or counted.get((x, y - 1), None) != blob:
                        sv[x] = True
                        sides += 1
                        #print("  new side left")
                else:
                    sv[x] = False
                
                (x_, y_) = (x, y - 1)
                if not in_grid(x_, y_) or counted.get((x_, y_), None) != blob:
                    if not sh or counted.get((x - 1, y), None) != blob:
                        sh = True
                        sides += 1
                        #print("  new side up")
                else:
                    sh = False
            else:
                (x_, y_) = (x - 1, y)
                if in_grid(x_, y_) and counted.get((x_, y_), None) == blob:
                    if not sv[x] or counted.get((x, y - 1), None) == blob:
                        sv[x] = True
                        sides += 1
                        #print("  new side left")
                else:
                    sv[x] = False
                
                (x_, y_) = (x, y - 1)
                if in_grid(x_, y_) and counted.get((x_, y_), None) == blob:
                    if not sh or counted.get((x - 1, y), None) == blob:
                        sh = True
                        sides += 1
                        #print("  new side up")
                else:
                    sh = False
                

    # print("Found ", c, " with ", area, perimeter, sides)
    total += area * perimeter
    total2 += area * sides



for j in range(Y):
    for i in range(X):
        if (i, j) not in counted:
            count(i, j)

print(total)
print(total2)

