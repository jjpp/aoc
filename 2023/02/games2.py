#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def is_possible(g):
    w = (g + ";").split()

    game_id = int(w[1][:-1])
    w = w[2:]

    m = {}

    while len(w) > 0:
        count = int(w[0])
        color = w[1][:-1]

        if color not in m or count > m[color]:
            m[color] = count
        w = w[2:]

    return m['red'] * m['green'] * m['blue']

print(sum([is_possible(l) for l in ls]))


