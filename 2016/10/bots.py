#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

b = {}
low = {}
high = {}
out = {}

upd = set()

def add_to(t, x, upd):
    if "o " in t:
        if t not in out:
            out[t] = []
        out[t].append(x)

    if t not in b:
        b[t] = []
    b[t] = sorted(b[t] + [x])
    if len(b[t]) == 2:
        upd.add(t)


prefix = {
        'bot': '',
        'output': 'o ',
}

for l in ls:
    c = l.split()

    if c[0] == "value":
        t = c[5]
        x = int(c[1])
        add_to(t, x, upd)
    else:
        low[c[1]] = prefix[c[5]] + c[6]
        high[c[1]] = prefix[c[10]] + c[11]


while len(upd) > 0:
    upd2 = set()
    for t in upd:
        if b[t][0] == 17 and b[t][1] == 61:
            print(f"17 vs 61 at {t}")
        add_to(low[t], b[t][0], upd2)
        add_to(high[t], b[t][1], upd2)

    upd = upd2 

print (out["o 0"][0] * out["o 1"][0] * out["o 2"][0])
