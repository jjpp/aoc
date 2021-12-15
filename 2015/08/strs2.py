#!/usr/bin/python3

import sys

diff = 0

for l in sys.stdin:
    l = l.strip()
    diff += 2 + sum([1 if c in ['\\', '"'] else 0 for c in l])

print(diff)

