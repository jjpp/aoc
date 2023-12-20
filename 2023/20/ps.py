#!/usr/bin/python3

import sys
from math import prod, lcm

ls = [l.strip() for l in sys.stdin]

ms = {}
s = {}

for l in ls:
    (m, ds) = l.split(' -> ')
    if m[0] in '%&':
        t = m[0]
        m = m[1:]
    else:
        t = '='
    ds = ds.split(', ')
    ms[m] = (t, ds)

for i in ms:
    if ms[i][0] == '&':
        s[i] = { m: 0 for m in ms if i in ms[m][1] }
    if ms[i][0] == '%':
        s[i] = 0

rx_low = False

cc = {}

def push(step):
    q = []
    q.append(('broadcaster', 0, 'button'))

    ss = [0, 0]


    def send(m, signal):
        for d in ms[m][1]:
            q.append((d, signal, m))

    while len(q) > 0:
        (m, signal, src) = q.pop(0)
        # print(f"{m} got {signal} from {src}")
        ss[signal] += 1

        if m not in ms:
            continue

        if ms[m][0] == '=':
            send(m, signal)

        elif ms[m][0] == '%':
            if signal == 0:
                s[m] = 1 - s.get(m, 0)
                send(m, s[m])
        elif ms[m][0] == '&':
            s[m][src] = signal
            out = 1 - prod(s[m].values())
            if m in s.get('ql', {}) and out == 1 and m not in cc:
                cc[m] = step + 1
                if len(cc) == len(s['ql']):
                    print(lcm(*list(cc.values())))
                    exit(0)
            send(m, out)
        else:
            print("should not happen")
            exit(1)
    return ss


seen = {}
c = 0
t = []

for i in range(0, 1000):
    t.append(push(len(t)))
    if len(t) > 1:
        t[-1][0] += t[-2][0]
        t[-1][1] += t[-2][1]

print(t[999][0] * t[999][1])

if 'ql' in ms and 'rx' in ms['ql'][1]:
    # in my input &ql is the only thing that outputs to 
    # rx. It has 4 independent inputs that are 1 on some
    # count. push() detects this and outputs the lcm of
    # those step counts.
    while True:
        i = i + 1
        push(i)
else:
    print("This is not the input we are looking for (for part 2).")

