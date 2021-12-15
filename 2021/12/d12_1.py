#!/usr/bin/python3

import sys

lns = [l.strip() for l in sys.stdin]

ps = {}

for l in lns:
    (f, t) = l.split('-')
    if not f in ps:
        ps[f] = set()
    if not t in ps:
        ps[t] = set()
    ps[f] |= set([t])
    ps[t] |= set([f])

seen = {}
paths = []

def dfs(n, seen, path):
    if n == 'end':
        paths.append(path + ['end'])
        return

    for n2 in ps[n]:
        if n2 not in seen or (n2[0].upper() == n2[0]):
            dfs(n2, seen | set([n]), path + [n])


dfs('start', set(), ['start'])

print(len(paths))
