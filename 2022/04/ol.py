#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


count = 0
for ps in ls:
    p1, p2 = ps.split(',')
    p1f, p1l = p1.split('-')
    p2f, p2l = p2.split('-')

    print(ps)
    print(p1f, p1l, p2f, p2l)

    if (int(p1f) >= int(p2f) and int(p1l) <= int(p2l)) or (int(p2f) >= int(p1f) and int(p2l) <= int(p1l)):
        print("in")
        count += 1

print(count)
