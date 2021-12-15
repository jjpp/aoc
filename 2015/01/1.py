#!/usr/bin/python3

import sys

line = sys.stdin.readline()
basement = -1

sum = 0
pos = 1
for c in line:
    if c in ['(', ')']:
        sum += 1 if c == '(' else -1
        if basement < 0 and sum == -1:
            basement = pos
        pos += 1

print(sum)
print(basement)

