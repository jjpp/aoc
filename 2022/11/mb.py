#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ms = []


while len(ls) > 0:
    m = {}
    ls.pop(0)
    itms = (ls.pop(0).split(': ', 2))[1].split(', ')
    items = [int(x) for x in itms]
    op = ls.pop(0).split(' = ', 2)[1]
    test = int(ls.pop(0).split(' ')[3])
    yes = int(ls.pop(0).split(' ')[5])
    no = int(ls.pop(0).split(' ')[5])
    ms.append({
        'items': items,
        'op': op,
        'test': test,
        'yes': yes,
        'no': no,
        'count': 0
    })
    if len(ls) > 0:
        ls.pop(0)

def monkey(m):
    mk = ms[m]
    for i in mk['items']:
        old = i
        new = eval(mk['op'])
        new = new // 3
        if new % mk['test'] == 0:
            ms[mk['yes']]['items'].append(new)
        else:
            ms[mk['no']]['items'].append(new)
    mk['count'] += len(mk['items'])
    mk['items'] = []

def monkeyround():
    for i in range(len(ms)):
        monkey(i)


for i in range(20):
    monkeyround()

cs = sorted([m['count'] for m in ms])

print(cs[-1] * cs[-2])

