#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

triplets = [[int(x) for x in l.split()] for l in ls]

triangles = [t for t in triplets if max(t) < sum(t) / 2]

print(len(triangles))

t2 = []

for i in range(0, len(triplets) // 3):
    for j in range(0, 3):
        t2.append([triplets[i*3][j], triplets[i*3+1][j], triplets[i*3+2][j]])

print(len([t for t in t2 if max(t) < sum(t) / 2]))

