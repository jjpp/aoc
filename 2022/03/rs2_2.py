#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

score = 0

while len(ls) > 0:
    seen = set(ls.pop(0)) & set(ls.pop(0)) & set(ls.pop(0))
    c = list(seen)[0]
    score += ord(c.upper()) - ord('A') + (27 if c.isupper() else 1)

print(score)
