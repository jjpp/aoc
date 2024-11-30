#!/usr/bin/env python3

I = 36000000
J = int(I / 10)

h = [0] * J
print(len(h))

m = J

for i in range(1, J):
    if i > m:
        continue
    for j in range(1, int(J / i) + 1):
        p = i * j
        if p >= m:
            continue
        h[p] += (i * 10)
        if h[p] >= I:
            if p < m:
                m = p
            print(p, " => ", h[p], i, j, m)
            break

print(m)


