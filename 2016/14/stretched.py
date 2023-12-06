#!/usr/bin/python3

import hashlib
import re

candidates = []
keys = []

salt = 'abc'
salt = 'ihaygndm'
idx = 0

triplet = re.compile(r"((.)\2\2)")
fiver = re.compile(r"((.)\2\2)\2\2")

def stretch(h):
    for i in range(0, 2017):
        h = hashlib.md5(h.encode('ascii')).hexdigest()
    return h

while len(keys) < 128:
    h = stretch(salt + str(idx))

    while len(candidates) > 0 and candidates[0][0] <= idx - 1000:
        print(f"at {idx}, {candidates[0]} is still without fiver, dropping")
        candidates.pop(0)

    fs = [m[0] for m in fiver.findall(h)]
    d = []
    if len(fs) > 0:
        print(f"at {idx} there are fivers: {fs}")
        for i in range(0, len(candidates)):
            if candidates[i][1] in fs:
                keys.append(candidates[i])
                print(candidates[i])
                d.append(i)

        for i in reversed(d):
            candidates.pop(i)

    t = triplet.search(h)
    if t:
        print(f"at {idx} found {t.group(1)}")
        candidates.append( (idx, t.group(1)) )

    idx += 1

keys = sorted(keys)
print(keys[0:10])
print(keys[63][0])


