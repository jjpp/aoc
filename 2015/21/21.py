#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

bhp = nums(ls[0])[0]
bd = nums(ls[1])[0]
ba = nums(ls[2])[0]


def wins(pd, pa, ph, bd, ba, bh):
    if ph <= 0: 
        return False

    return not wins(bd, ba, bh - max(pd - ba, 1), pd, pa, ph)

armors = [
        (0, 0),
        (13, 1),
        (31, 2),
        (53, 3),
        (75, 4), 
        (102, 5)
    ]

weapons = [
        (8, 4),
        (10, 5),
        (25, 6),
        (40, 7),
        (74, 8)
]

weapons2 = [
        (0, 0),
        (25, 1),
        (50, 2),
        (100, 3),
        (75, 3),
        (125, 4),
        (150, 5)
]

armors2 = [
        (0, 0),
        (20, 1),
        (40, 2),
        (80, 3),
        (60, 3),
        (100, 4),
        (120, 5)
]

minwin = 99999
maxlose = 0
for a in armors:
    for w in weapons:
        for a2 in armors2:
            for w2 in weapons2:
                price = a[0] + w[0] + a2[0] + w2[0]
                if wins(w[1] + w2[1], a[1] + a2[1], 100, bd, ba, bhp):
                    if price < minwin:
                        print(a, w, a2, w2)
                        minwin = price
                else:
                    if price > maxlose:
                        maxlose = price

print(minwin)
print(maxlose)
