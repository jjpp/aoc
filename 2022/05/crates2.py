#!/usr/bin/python3

import sys

ls = [l for l in sys.stdin]

stacks = []

while '[' in ls[0]:
    l = ls.pop(0)
    for s in range(0, (len(l) - 1) // 4 + 1):
        c = l[s * 4 + 1]
        if c != ' ':
            while len(stacks) <= s:
                stacks.append([])
            stacks[s].insert(0, c)

ls.pop(0)
ls.pop(0)

while len(ls) > 0:
    (_, count, _, src, _ , dst) = ls.pop(0).split(' ')
    [count, src, dst] = [int(x) for x in [count, src, dst]]
    src -= 1
    dst -= 1

    b = stacks[src][-count:]
    for i in range(0, count):
        stacks[dst].append(b.pop(0))
        stacks[src].pop()

print("".join([stacks[i][-1] for i in range(0, len(stacks))]))


