#!/usr/bin/python3

import sys

inp = sys.stdin.read()


scrs = []

sensors = set()
scanners = {}
dirs = {}

# https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR

def dir(p, d):
    (x, y, z) = p
    return [
        ( x,  y,  z),
        ( x, -y, -z),
        (-x,  y, -z),
        (-x, -y,  z),
        ( x,  z, -y),
        ( x, -z,  y),
        (-x,  z,  y),
        (-x, -z, -y),
        ( y,  x, -z),
        ( y, -x,  z),
        (-y,  x,  z),
        (-y, -x, -z),
        ( y,  z,  x),
        ( y, -z, -x),
        (-y,  z, -x),
        (-y, -z,  x),
        ( z,  x,  y),
        ( z, -x, -y),
        (-z,  x, -y),
        (-z, -x,  y),
        ( z,  y, -x),
        ( z, -y,  x),
        (-z,  y,  x),
        (-z, -y, -x),
    ][d]



for scr in inp.split('\n\n'):
    lns = scr.split('\n')
    scrs.append([[int(x) for x in l.split(',')] for l in lns[1:] if len(l) > 0])


sensors = set([tuple(t) for t in scrs[0]])
scanners[0] = (0, 0, 0)
dirs[0] = 0

def can_match(s, i, sensors):
    print(f"Matching scanner {i} with existing {len(sensors)} sensors")
    for d in range(24):
        # print(f"  direction {d}")
        pts = [list(dir(b, d)) for b in s]
        for p0 in pts:
            #print(f"    {p0} as a relative start")
            for p1 in sensors.copy():
                (x, y, z) = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
                #print(f"      {p1} as reference beacon, scanner should be at {x},{y},{z}")
                all_bs = set([(p[0] + x, p[1] + y, p[2] + z) for p in pts])
                # fixme: check if nothing in range that should not be?

                #print(f"        {len(all_bs & sensors)} common beacons")

                if len(all_bs & sensors) > 11:
                    print(f"Scanner {i} at {x},{y},{z} ({d})")
                    sensors |= all_bs
                    scanners[i] = (x, y, z)
                    dirs[i] = d
                    return True
    return False


q = list(range(1, len(scrs)))
while len(q) > 0:
    i = q.pop(0)
    if not can_match(scrs[i], i, sensors):
        q.append(i)


print(len(sensors))

print(scanners)

mhd = 0

for (i, a) in scanners.items():
    for (j, b) in scanners.items():
        if i != j:
            mhd = max(mhd, abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]))

print(mhd)

