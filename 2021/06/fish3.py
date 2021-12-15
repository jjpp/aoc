#!/usr/bin/python3

import sys

ln = sys.stdin.readline()

fish = [int(x) for x in ln.strip().split(',')]

ages = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

for f in fish:
    ages[f] += 1


def iterate(ages):
    s = ages.pop(0)
    ages[6] += s
    ages.append(s)
    return ages


for n in range(257):
    print(n, sum(ages))
    ages = iterate(ages)

