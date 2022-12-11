#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ms = []

mod = 1


while len(ls) > 0:
    m = {}
    ls.pop(0)
    itms = (ls.pop(0).split(': ', 2))[1].split(', ')
    items = [int(x) for x in itms]
    op = eval("lambda old: " + ls.pop(0).split(' = ', 2)[1])
    test = int(ls.pop(0).split(' ')[3])
    mod *= test
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
        new = mk['op'](i) % mod
        if new % mk['test'] == 0:
            ms[mk['yes']]['items'].append(new)
        else:
            ms[mk['no']]['items'].append(new)
    mk['count'] += len(mk['items'])
    mk['items'] = []

def monkeyround():
    for i in range(len(ms)):
        monkey(i)

for i in range(10000):
    monkeyround()

cs = sorted([m['count'] for m in ms])

print(cs[-1] * cs[-2])

