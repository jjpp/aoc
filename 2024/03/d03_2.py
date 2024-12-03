#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]
s = 0
enabled = True

for l in ls:
    while True:
        m = re.search(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\))(.*)$", l)
        if m:
            cmd = m.group(1)
            if cmd.startswith("mul"):
                if enabled:
                    s += int(m.group(2)) * int(m.group(3))
            elif cmd == "do()":
                enabled = True
            elif cmd == "don't()":
                enabled = False
            else:
                print("hm: ", m)

            l = m.group(4)
        else:
            break

print(s)
