#!/usr/bin/python3

import sys

diff = 0

for l in sys.stdin:
    l = l.strip()
    diff += (len(l) - len(eval(l)))

print(diff)

