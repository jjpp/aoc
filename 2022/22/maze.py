#!/usr/bin/python3

import sys

ls = [l for l in sys.stdin]

R = ls.index("\n")
C = max([len(l) for l in ls[0:R]])

m = {}
for x in range(C + 2):
    m[complex(x, 0)] = ' '
    m[complex(x, R + 1)] = ' '

for y in range(1, R + 1):
    m[complex(0, y)] = ' '
    m[complex(C + 1, y)] = ' '
    for x in range(C):
        if x < len(ls[y - 1]) - 1:
            m[complex(x + 1, y)] = ls[y - 1][x]
        else:
            m[complex(x + 1, y)] = ' '

R += 2
C += 2

arrow = { 1: '>', -1: '<', -1j: '^', 1j: 'v' }
dirs = { 1: 0, 1j: 1, -1: 2, -1j: 3 }

def printm(p, d):
    for r in range(R):
        out = ""
        for c in range(C):
            q = complex(c, r)
            if q == p:
                out += arrow[d]
            else:
                out += m[q]
        print('|' + out + '|')



d = 1 + 0j
p = complex(ls[0].index('.') + 1, 1)


cmds = list(ls[-1].strip())

while len(cmds) > 0:
    if cmds[0] in 'LR':
        if cmds[0] == 'L':
            d = d * -1j
        else:
            d = d * 1j
        cmds.pop(0)
    else:
        s = 0
        while len(cmds) > 0 and cmds[0] in '0123456789':
            s *= 10
            s += int(cmds.pop(0))
        
        for _ in range(s):
            pn = p + d
            if m[pn] == ' ':
                pn = p
                while m[pn - d] != ' ':
                    pn -= d
            if m[pn] == '.':
                p = pn

print(int(1000 * p.imag + 4 * p.real + dirs[d]))

            
