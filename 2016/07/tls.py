#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def abba(s):
    for i in range(3, len(s)):
        if s[i - 3] == s[i] and s[i-2] == s[i-1] and s[i-1] != s[i]:
            return True
    return False

def check(l):
    found = 0
    while len(l) > 0:
        _l = l.split('[', 1)
        if abba(_l[0]):
            found = 1
        l = _l[1] if len(_l) > 1 else ""
        _l = l.split(']', 1)
        if abba(_l[0]):
            return 0
        l = _l[1] if len(_l) > 1 else ""

    return found

print(sum([check(l) for l in ls]))

