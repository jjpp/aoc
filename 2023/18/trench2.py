#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ds = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
}

t = {}

x = 1
y = 1

minx = maxx = miny = maxy = 1

v = [(1, 1)]
d_ = []
l_ = []
xs = set([1])
ys = set([1])

dss = 'RDLU'
for l in ls:
    (d, l, c) = l.split()
    d = dss[int(c[-2:-1])]
    l = int(c[2:-2], 16)

    (x, y) = (x + ds[d][0] * l, y + ds[d][1] * l)
    xs.add(x)
    xs.add(x + 1)
    ys.add(y)
    ys.add(y + 1)
    v.append((x, y))
    d_.append(d)
    l_.append(l)

    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

xs = sorted(list(xs))
ys = sorted(list(ys))

(x, y) = (1, 1)
for i in range(0, len(v) - 1):
    d = d_[i]
    l = l_[i]
    x_ = xs.index(x)
    y_ = ys.index(y)
    while (xs[x_] != v[i + 1][0] or ys[y_] != v[i + 1][1]):
        t[x_, y_] = (xs[x_ + 1] - xs[x_]) * (ys[y_ + 1] - ys[y_])
        (x_, y_) = (x_ + ds[d][0], y_ + ds[d][1])
    (x, y) = v[i + 1]

#for y in range(0, len(ys)):
#    print("".join(["#" if (x, y) in t else '.' for x in range(0, len(xs))]))


#for y in range(miny, maxy + 1):
#    print("".join(['#' if (x, y) in t else '.' for x in range(minx, maxx + 1)]))

def fill(x, y, v):
    q = [(x, y)]
    while len(q) > 0:
        (x, y) = q.pop()
        if x < 0 or x >= len(xs) or y < 0 or y > len(ys):
            continue
        if (x, y) in t:
            continue

        t[x, y] = v 
        for d in ds:
            q.append((x + ds[d][0], y + ds[d][1]))

for y in range(0, len(ys)):
    fill(0, y, 0)
    fill(len(xs) - 1, y, 0)

for x in range(0, len(xs)):
    fill(x, 0, 0)
    fill(x, len(ys) - 1, 0)

for y in range(0, len(ys) - 1):
    for x in range(0, len(xs) - 1):
        if (x, y) not in t:
            t[x, y] = (xs[x + 1] - xs[x]) * (ys[y + 1] - ys[y]) 

#for y in range(0, len(ys)):
#    print("".join(["#" if t[x, y] > 0 else '.' for x in range(0, len(xs))]))


print(sum(t.values()))

