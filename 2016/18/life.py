#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]


def iter(l):
    o = ""
    for i in range(0, len(l)):
        p = ("." + l + ".")[i:i+3]
        o += "^" if p in ["^^.", ".^^", "^..", "..^"] else "."

    return o

s = 0
l = ls[0]
for i in range(0, 400000):
    s += len([x for x in l if x == "."]) 
    print(l)
    l = iter(l)

print(s)

