#!/usr/bin/python3

import sys

ln = sys.stdin.readline()

fish = [int(x) for x in ln.strip().split(',')]

def iterate(fs):
    out = []
    for f in fs:
        if f == 0:
            out.append(6)
            out.append(8)
        else:
            out.append(f - 1)
    return out

for x in range(80):
    fish = iterate(fish)


print(len(fish))

for x in range(256 - 80):
    fish = iterate(fish)


print(len(fish))
