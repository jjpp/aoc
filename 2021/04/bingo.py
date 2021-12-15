#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ns = [int(n) for n in ls[0].split(',')]
bs = []

for b in range((len(ls) - 1) // 6):
    b_ = []
    for r in range(5):
        b_.append([int(n) for n in ls[2 + (b*6) + r].split()])
    bs.append(b_)


chosen = set()

def check_win(b, ln, bn):
    won = False
    for i in range(5):
        row = col = True
        for j in range(5):
            row = row and b[i][j] in chosen
            col = col and b[j][i] in chosen
        if row or col:
            won = True
            break
    if won:
        score = 0
        for i in range(5):
            for j in range(5):
                if b[i][j] not in chosen:
                    score += b[i][j]
        print(bn, "winning score", score * ln)
    return won

wb = set()

for n in ns:
    chosen |= set([n])

    for (i, b) in enumerate(bs):
        if (i not in wb):
            if check_win(b, n, i):
                wb |= set([i])



