#!/usr/bin/env python3

import sys

prev = 9999
count = 0

b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

for l in sys.stdin:
    a = int(l.strip())
    if a + b + c > prev:
        count += 1
    prev = a + b + c
    c = b
    b = a

print(count)

