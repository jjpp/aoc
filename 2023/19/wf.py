#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

wf = {}

wfc = ls.index("")

for i in range(0, ls.index("")):
    wfn = ls[i][0:ls[i].index('{')]
    rs = ls[i][ls[i].index('{') + 1 : -1].split(',')
    rs[-1] = ":" + rs[-1]
    wf[wfn] = [r.split(':') for r in rs]

def eval_part(s):
    (x, m, a, s) = [int(p[2:]) for p in s[1:-1].split(',')]

    w = 'in'
    while True:
        result = None
        for r in wf[w]:
            if r[0] == '':
                result = r[1]
            else:
                if eval(r[0]):
                    result = r[1]
                    break

        if result == 'A':
            return x + m + a + s
        elif result == 'R':
            return 0
        else:
            w = result


print(sum([eval_part(l) for l in ls[wfc + 1:]]))

            
