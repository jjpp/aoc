#!/usr/bin/python3

import sys
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

b = {}
q = PriorityQueue()

X = len(ls[0])
Y = len(ls)

LAST = (X - 1, Y - 1)

q.put((int(ls[0][1]), 1, 0, 1, 0, 1))
q.put((int(ls[1][0]), 0, 1, 0, 1, 1))

while not q.empty():
    (cost, x, y, dx, dy, s3) = q.get()

    if (x, y) not in b:
        b[x, y] = {}

    if (dx, dy, s3) in b[x, y] and b[x, y][dx, dy, s3] <= cost:
        continue

    b[x, y][dx, dy, s3] = cost

    if (x, y) == LAST and s3 > 3:
        break

    x_ = x - dy
    y_ = y - dx

    if x_ >= 0 and x_ < X and y_ >= 0 and y_ < Y and s3 > 3:
        q.put((cost + int(ls[y_][x_]), x_, y_, -dy, -dx, 1))

    x_ = x + dx
    y_ = y + dy

    if x_ >= 0 and x_ < X and y_ >= 0 and y_ < Y and s3 < 10:
        q.put((cost + int(ls[y_][x_]), x_, y_, dx, dy, s3 + 1))

    x_ = x + dy
    y_ = y + dx
    if x_ >= 0 and x_ < X and y_ >= 0 and y_ < Y and s3 > 3:
        q.put((cost + int(ls[y_][x_]), x_, y_, dy, dx, 1))

def path(x, y, c):
    if x == 0 and y == 0:
        return []
    else:
        dm = sorted([d for d in b[x, y].keys() if b[x, y][d] == c], key = lambda d: b[x, y][d])
        if len(dm) == 0:
            print("could not backtrack at", x, y, b[x, y])
            return [(x, y, c)]
        return path(x - dm[0][0], y - dm[0][1], c - int(ls[y][x])) + [(x, y, dm[0][2], c)]
        
m = min([b[LAST][v] for v in b[LAST] if v[2] > 3])

#print(path(X - 1, Y - 1, m))

print(m)



