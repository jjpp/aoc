#!/usr/bin/python3

# part 1

import sys

ls = [l.strip() for l in sys.stdin]

def is_safe(x):
    xs = [int(x_) for x_ in x.split(' ')]

    ds = [xs[i] - xs[i - 1] for i in range(1, len(xs))]
    return all([d in [-3, -2, -1] for d in ds]) or all([d in [1, 2, 3] for d in ds])


print(sum([1 for x in ls if is_safe(x)]))
