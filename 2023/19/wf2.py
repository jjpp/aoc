#!/usr/bin/python3

import sys
import math
from copy import deepcopy

ls = [l.strip() for l in sys.stdin]

wf = {}

wfc = ls.index("")

for i in range(0, ls.index("")):
    wfn = ls[i][0:ls[i].index('{')]
    rs = ls[i][ls[i].index('{') + 1 : -1].split(',')
    rs[-1] = ":" + rs[-1]
    wf[wfn] = [r.split(':') for r in rs]

def eval_part():
    q = []
    s = 0
    q.append(('in', { 'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000) }))
    while len(q) > 0:
        (w, v) = q.pop()
        if w == 'A':
            s += math.prod([(v[x][1] - v[x][0] + 1) if v[x][1] >= v[x][0] else 0 for x in 'xmas'])
            continue
        if w == 'R':
            continue

        for r in wf[w]:
            if r[0] == '':
                q.append((r[1], v))
            else:
                l = r[0][0]
                op = r[0][1]
                val = int(r[0][2:])

                if op == '<':
                    if val < v[l][0]:
                        ...
                    elif val < v[l][1]:
                        q.append((r[1], { **v, l: (v[l][0], val - 1) }))
                        v.update({ l: (val, v[l][1]) })
                    else:
                        q.append((r[1], v))
                        break
                elif op == '>':
                    if val > v[l][1]:
                        ...
                    elif val > v[l][0]:
                        q.append((r[1], { **v, l: (val + 1, v[l][1]) }))
                        v.update({ l: (v[l][0], val) })
                    else:
                        q.append((r[1], v))
                        break
                else:
                    print("We should not reach here")
                    exit(1)

    return s

print(eval_part())
