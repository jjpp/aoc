#!/usr/bin/python3

# part 1

import sys

ls = [l.strip() for l in sys.stdin]

bs = []

fid = 0
free = False
for l in ls[0]:
    bc = int(l)
    if free:
        bs += [None] * bc
    else:
        bs += [fid] * bc
        fid += 1
    free = not free

while None in bs:
    b = bs.pop()
    if b == None:
        continue

    bs[bs.index(None)] = b

cs = sum([ p * v for (p, v) in zip(range(len(bs)), bs) if v != None])

print(cs)

