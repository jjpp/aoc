#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

l = ls.pop(0)

for i in range(14, len(l)):
    if len(set(l[i-14:i])) == 14:
        print(i)
        break


