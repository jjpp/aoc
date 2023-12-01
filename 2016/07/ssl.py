#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def aba(s):
    out = []
    for i in range(2, len(s)):
        if s[i - 2] == s[i] and s[i-1] != s[i]:
            out += [s[i-2:i+1]]
    return out

def check(l):
    abas = []
    babs = []
    while len(l) > 0:
        _l = l.split('[', 1)
        abas += aba(_l[0])
        l = _l[1] if len(_l) > 1 else ""

        _l = l.split(']', 1)
        babs += aba(_l[0])
        l = _l[1] if len(_l) > 1 else ""

    for a in abas:
        if a[1] + a[0] + a[1] in babs:
            return 1

    return 0

print(sum([check(l) for l in ls]))

