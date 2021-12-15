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

paths = []

def dfs(n, seen, twice, path):
    if n == 'end':
        paths.append("-".join(path + ['end']))
        return

    for n2 in ps[n]:
        if n2 not in seen or (len(twice) == 0) or (n2[0].upper() == n2[0]):
            if n2 != 'start':
                seennew = seen | set([n])
                if (n2[0].upper() != n2[0]) and n2 in seen:
                    twicenew = set([n2])
                else:
                    twicenew = twice

                dfs(n2, seennew, twicenew, path + [n])


dfs('start', set(), set(), [])

print("-----")
print("\n".join(sorted(paths)))

print(len(paths))
