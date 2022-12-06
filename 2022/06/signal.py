#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

l = ls.pop(0)

for i in range(4, len(l)):
    if len(set(l[i-4:i])) == 4:
        print(i)
        break


