#!/usr/bin/python3

# part 2

import sys

ls = [l.strip() for l in sys.stdin]

bs = []
frees = []
files = []

fid = 0
free = False
for l in ls[0]:
    bc = int(l)
    if free:
        frees.append((len(bs), bc))
        bs += [None] * bc
    else:
        files.append((len(bs), bc, fid))
        bs += [fid] * bc
        fid += 1
    free = not free

for fileidx in reversed(range(len(files))):
    file = files[fileidx]
    for freeidx in range(len(frees)):
        free = frees[freeidx]
        if free[0] >= file[0]:
            break

        if free[1] >= file[1]:
            bs[free[0]:free[0] + file[1]] = [file[2]] * file[1]
            bs[file[0]:file[0] + file[1]] = [None] * file[1]
            if free[1] == file[1]:
                del frees[freeidx]
            else:
                frees[freeidx] = (free[0] + file[1], free[1] - file[1])
            break

cs = sum([ p * v for (p, v) in zip(range(len(bs)), bs) if v != None])

print(cs)

