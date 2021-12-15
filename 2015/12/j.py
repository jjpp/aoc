#!/usr/bin/python3

import json
import sys

j = sys.stdin.readline().strip()

d = json.loads(j)

def nums(d):
    if isinstance(d, int):
        return d
    if isinstance(d, list):
        return sum([nums(i) for i in d])
    if isinstance(d, dict):
        return sum([nums(v) for v in d.values()])
    if isinstance(d, str):
        return 0
    raise "unexpexted element: " + d
    return 0

print(nums(d))

