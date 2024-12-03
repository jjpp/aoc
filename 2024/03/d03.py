#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]
s = 0

for l in ls:
    while True:
        m = re.search(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)(.*)$", l)
        if m:
            s += int(m.group(1)) * int(m.group(2))
            l = m.group(3)
        else:
            break

print(s)
