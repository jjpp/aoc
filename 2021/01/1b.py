#!/usr/bin/env python3

import sys

ls = [int(l.strip()) for l in sys.stdin]

print(sum([1 for (a, b) in  zip(ls, ls[1:]) if a < b]))

ws = [sum(z) for z in zip(ls, ls[1:], ls[2:])]

print(sum([1 for (a, b) in  zip(ws, ws[1:]) if a < b]))

