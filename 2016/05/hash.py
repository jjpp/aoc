#!/usr/bin/python3

import sys
import hashlib

ls = [l.strip() for l in sys.stdin]

doorid = ls[0]

def code(door):
    i = 0
    out = ""

    while len(out) < 8:
        t = hashlib.md5((door + str(i)).encode()).hexdigest()
        if t[0:5] == '00000':
            out += t[5]
            print(out, "at", i)
        i += 1

    return out

def code2(door):
    i = 0
    out = [None, None, None, None, None, None, None, None]

    while None in out:
        t = hashlib.md5((door + str(i)).encode()).hexdigest()
        if t[0:5] == '00000':
            pos = ord(t[5]) - ord('0')
            if pos < 8 and out[pos] == None:
                out[pos] = t[6]
            print(out, "at", i)
        i += 1

    return "".join(out)

print(code(doorid))
print(code2(doorid))

