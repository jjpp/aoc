#!/usr/bin/python3

import sys
from collections import Counter
from functools import reduce
from operator import mul, or_

ls = [l.strip() for l in sys.stdin]

max_color = Counter({
        'red': 12,
        'green': 13,
        'blue': 14
})

def is_possible(g):
    pairs = [p.split() for p in g.replace(";", ",").replace(":", ",").split(",")]

    game_id = int(pairs.pop(0)[1])

    m = reduce(or_, [Counter({p[1]: int(p[0])}) for p in pairs])

    return (game_id if m <= max_color else 0, reduce(mul, m.values()))


print(reduce(lambda a, b: tuple(map(sum, zip(a, b))), [is_possible(l) for l in ls]))


