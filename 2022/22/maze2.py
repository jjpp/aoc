#!/usr/bin/python3

import sys

ls = [l for l in sys.stdin]

R = ls.index("\n")
C = max([len(l) for l in ls[0:R]])
S = min([len(l.strip()) for l in ls[0:R]])

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
arrow2 = { 1: ')', -1: '(', -1j: 'A', 1j: 'V' }
dirs = { 1: 0, 1j: 1, -1: 2, -1j: 3 }

def printm(p, d, n):
    for r in range(R):
        out = ""
        for c in range(C):
            q = complex(c, r)
            if False and q == p:
                out += arrow[d]
            else:
                d_ = "".join([ arrow[d] for d in dirs if (q, d) in n ])
                d2_ = "".join([ arrow2[d] for d in dirs if (q, d) in n.values() ])
                if d_ != '':
                    if len(d_) > 1:
                        out += '*'
                    else:
                        out += d_
                elif d2_ != '':
                    if len(d2_) > 1:
                        out += 'x'
                    else:
                        out += d2_ 
                else:
                    out += m[q]
        print('|' + out + '|')



d = 1 + 0j
p = complex(ls[0].index('.') + 1, 1)


cmds = list(ls[-1].strip())

n = {}

if S <= 4:
    # test input, not finished
    for i in range(S):
        # 1 up -> 2 down
        n[complex(1 + 2*S + i, 0), -1j] = (complex(1 + i, S + 1), 1j)
        # 1 right -> 6 left
        n[complex(3*S + 1, 1 + i), 1] = (complex(4*S, 1 + 2*S + i) -1)
        # 4 right -> 6 down
        n[complex(3*S + 1, 1 + S + i), 1] = (complex(3*S + 1 + i, 1 + 2*S), 1j)
        # 6 up -> 4 left
        n[complex(3*S + 1 + i, 2*S), -1j] = (complex(3*S, 1 + S + i), -1)
        # 6 right -> 1 left
        n[complex(4*S + 1, 1 + 2*S + i), 1] = (complex(3*S, 1 + i), -1)
        # 6 down -> 2 right
        
else:
    for i in range(S):
        # 1 up -> 6 right:
        n[complex(1 + S + i, 0), -1j] = (complex(1, 1 + 3 * S + i), 1)
        # 2 up -> 6 up:
        n[complex(1 + 2*S + i, 0), -1j] = (complex(1 + i, 4 * S), -1j)
        # 2 right -> 5 left
        n[complex(1 + 3*S, 1 + i), 1] = (complex(2*S, 3*S - i), -1)
        # 2 down -> 3 left
        n[complex(1 + 2*S + i, 1 + S), 1j] = (complex(2*S, 1 + S + i), -1)
        # 3 right -> 2 up
        n[complex(1 + 2*S, 1 + S + i), 1] = (complex(1 + 2*S + i, S), -1j)
        # 5 right -> 2 left
        n[complex(2*S + 1, 3*S - i), 1] = (complex(3*S, 1 + i), -1)
        # 5 down -> 6 left
        n[complex(1 + S + i, 3*S + 1), 1j] = (complex(S, 3*S + 1 + i), -1)
        # 6 right -> 5 up
        n[complex(S+1, 3*S + 1 + i), 1] = (complex(1 + S + i, 3*S), -1j)
        # 6 down -> 2 down
        n[complex(1 + i, 4 * S + 1), 1j] = (complex(1 + 2*S + i, 1), 1j)
        # 6 left -> 1 down
        n[complex(0, 1 + 3 * S + i), -1] = (complex(1 + S + i, 1), 1j)
        # 4 left -> 1 right
        n[complex(0, 1 + 2 * S + i), -1] = (complex(1 + S, S - i), 1)
        # 4 up -> 3 right
        n[complex(i + 1, 2 * S), -1j] = (complex(1 + S, 1 + S + i), 1)
        # 3 left -> 4 down
        n[complex(S, 1 + S + i), -1] = (complex(i + 1, 2 * S + 1), 1j)
        # 1 left -> 4 right
        n[complex(S, 1 + i), -1] = (complex(1, 3 * S - i), 1)


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
            d_ = d
            if m[pn] == ' ':
                (pn, d_) = n[pn, d]
            if m[pn] == '.':
                p = pn
                d = d_

print(int(1000 * p.imag + 4 * p.real + dirs[d]))

