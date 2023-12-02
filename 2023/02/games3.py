#!/usr/bin/python3

import sys
from collections import Counter
from functools import reduce
from operator import mul

ls = [l.strip() for l in sys.stdin]

max_color = Counter({
        'red': 12,
        'green': 13,
        'blue': 14
})

def is_possible(g):
    pairs = g.replace(";", ",").replace(":", ",").split(",")

    game_id = int(pairs[0].split()[1])

    m = reduce(lambda a, b: a | b, [Counter({p.split()[1]: int(p.split()[0])}) for p in pairs[1:]])

    return (game_id if m <= max_color else 0, reduce(mul, m.values()))


print(sum([is_possible(l)[0] for l in ls]))
print(sum([is_possible(l)[1] for l in ls]))


