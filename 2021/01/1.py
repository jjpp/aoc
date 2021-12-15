#!/usr/bin/env python3

import sys

prev = 9999
count = 0

for l in sys.stdin:
    a = int(l.strip())
    if a > prev:
        count += 1
    prev = a

print(count)

