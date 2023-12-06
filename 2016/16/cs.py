#!/usr/bin/python3


def invert(s):
    return "".join(["1" if b == '0' else '0' for b in s])

def fill(s, l):
    while len(s) < l:
        s = s + '0' + invert(reversed(s))

    return s[0:l]

def checksum(s):
    while (len(s) % 2 == 0):
        s = "".join(["1" if a == b else "0" for (a, b) in zip(s[0::2], s[1::2])])
    return s

print(checksum(fill("11110010111001001", 272)))
print(checksum(fill("11110010111001001", 35651584)))
