#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

cave = {}

deepest = 0
leftmost = 500
rightmost = 500

for l in ls:
    ps = l.split(' -> ')
    [c,r] = [int(x) for x in ps.pop(0).split(',')]
    cave[complex(c, r)] = '#'

    deepest = max(deepest, r)
    leftmost = min(leftmost, c)
    rightmost = max(rightmost, c)
    
    while len(ps) > 0:
        [nc, nr] = [int(x) for x in ps.pop(0).split(',')]

        while c != nc or r != nr:
            if c != nc:
                c += (nc - c) // abs(nc - c)
            elif r != nr:
                r += (nr - r) // abs(nr - r)
            else:
                print("Should not happen")

            cave[complex(c, r)] = '#'
            deepest = max(deepest, r)
            leftmost = min(leftmost, c)
            rightmost = max(rightmost, c)

def print_cave():
    for r in range(deepest + 1):
        o = ""
        for c in range(leftmost, rightmost + 1):
            p = complex(c, r)
            o += "." if p not in cave else cave[p]
        print(o)


def sand():
    (c, r) = (500, 0)

    while (complex(c, r + 1) not in cave or complex(c - 1, r + 1) not in cave or complex(c + 1, r + 1) not in cave) and r <= (deepest + 1):
        if complex(c, r + 1) not in cave:
            r += 1
            continue
        if complex(c - 1, r + 1) not in cave:
            r += 1
            c -= 1
            continue
        if complex(c + 1, r + 1) not in cave:
            r += 1
            c += 1
            continue
        print("Should not happen either")

    if r <= deepest:
        cave[complex(c, r)] = 'o'
        return True
    else:
        return False


count = 0
while sand():
    count += 1

# print_cave()


print(count)






