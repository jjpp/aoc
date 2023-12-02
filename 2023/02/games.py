#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

max_color = {
        'red': 12,
        'green': 13,
        'blue': 14
}

def is_possible(g):
    w = (g + ";").split()

    game_id = int(w[1][:-1])
    w = w[2:]

    while len(w) > 0:
        count = int(w[0])
        color = w[1][:-1]

        if count > max_color[color]:
            return 0
        w = w[2:]

    return game_id

print(sum([is_possible(l) for l in ls]))


