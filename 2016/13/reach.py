#!/usr/bin/python3

from queue import PriorityQueue

num = 1358

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

walls = {}
def is_wall(x, y):
    if (x, y) in walls:
        return walls[x, y]

    if x < 0 or y < 0:
        return True

    z = x*x + 3*x + 2*x*y + y + y*y + num
    walls[x, y] = z.bit_count() & 1 == 1
    return walls[x, y]

q = PriorityQueue()
dist = {}
q.put((0, (1, 1)))

while not q.empty():
    (d, (x, y)) = q.get()

    if d > 50:
        continue

    if (x, y) in dist and dist[x, y] <= d:
        continue

    dist[x, y] = d

    for dr in range(0, 4):
        x_ = x + dx[dr]
        y_ = y + dy[dr]

        if ((x_, y_) in dist and dist[x_, y_] < d + 1) or is_wall(x_, y_):
            continue

        q.put((d + 1, (x_, y_)))

print(len(dist.keys()))

