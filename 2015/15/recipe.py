#!/usr/bin/python3

import sys
import functools

igs = {}

for line in sys.stdin:
    [name, _, cap, _, dur, _, fla, _, txt, _, cal] = line.strip().split(' ')
    name = name.strip(':')
    cap = int(cap.strip(','))
    dur = int(dur.strip(','))
    fla = int(fla.strip(','))
    txt = int(txt.strip(','))
    cal = int(cal)

    igs[name] = [cap, dur, fla, txt, cal]


ams = {}

def allocate(uuigs, uuspace):
    if len(uuigs) == 0:
        if sum([igs[k][4] * ams[k] for k in igs.keys()]) != 500:
            return 0
        score = functools.reduce(lambda x,y: x*y, [max(0, sum([igs[k][i] * ams[k] for k in igs.keys()])) for i in range(0,4)], 1)
        return score

    k = uuigs[0]
    max_score = 0
    for amt in range(0, uuspace + 1):
        ams[k] = amt
        max_score = max(allocate(uuigs[1:], uuspace - amt), max_score)

    return max_score


max_score = allocate([*igs.keys()], 100)

print(max_score)
