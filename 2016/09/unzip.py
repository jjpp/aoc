#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

_in = "\n".join(ls)
_out = ""

while (len(_in) > 0):
    if "(" in _in:
        i = _in.index("(")
    else:
        i = len(_in)

    if i > 0:
        _out += _in[:i]
        _in = _in[i:]
        continue
    
    if i == 0:
        i = _in.index(")")
        (a, b) = _in[1:i].split("x")
        a = int(a)
        b = int(b)
        _in = _in[i+1:]
        _out += (_in[0:a] * b)
        _in = _in[a:]
        continue

print(_out)
print(len(_out))

