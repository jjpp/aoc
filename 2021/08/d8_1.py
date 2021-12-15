#!/usr/bin/python3

import sys

total = 0
for l in sys.stdin:
    l = l.strip()
    (a, b) = l.split(' | ')
    total += sum([1 for w in b.split(' ') if len(w) in { 2, 3, 7, 4 }])

print(total)
    
