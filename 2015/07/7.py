#!/usr/bin/python3

import sys

ws = {}

def memoize(w, v):
    ws[w] = v
    return v

def get_wire(w):
    if w.isdigit():
        return int(w)

    if isinstance(ws[w], int):
        return ws[w]

    if ws[w].isdigit():
        return memoize(w, int(ws[w]))

    g = ws[w].split(' ')

    if len(g) == 1:
        return memoize(w, get_wire(g[0]))

    if len(g) == 2 and g[0] == 'NOT':
        return memoize(w, 65535 ^ get_wire(g[1]))

    if g[1] == 'AND':
        return memoize(w, get_wire(g[0]) & get_wire(g[2]))

    if g[1] == 'OR':
        return memoize(w, get_wire(g[0]) | get_wire(g[2]))

    if g[1] == 'LSHIFT':
        return memoize(w, (get_wire(g[0]) << get_wire(g[2])) % 65536)

    if g[1] == 'RSHIFT':
        return memoize(w, get_wire(g[0]) >> get_wire(g[2]))

    raise "Unknown op: " + ws[w]

for l in sys.stdin:
    [src, w] = l.strip().split(' -> ')
    ws[w] = src

orig_ws = {**ws}
b = get_wire('a')

print(b)

ws = orig_ws
ws['b'] = b

print(get_wire('a'))

