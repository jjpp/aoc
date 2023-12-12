#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def cnt(l):
    (p, cs) = l.split()
    cs = [int(c) for c in cs.split(',')]

    p = "?".join([p] * 5)
    cs = cs * 5

    cache = {}

    def _check(p, cs, c, path, sumcs, und):
        lencs = len(cs)
        if (p, lencs, c) in cache:
            return cache[p, lencs, c]
        v = check(p, cs, c, path, sumcs, und)
        cache[p, lencs, c] = v
        return v

    def check(p, cs, c, path, sumcs, und):
        lencs = len(cs)
        if p == "":
            if lencs > 1:
                return 0
            elif lencs == 1:
                if cs[0] == c:
                    return 1
                else:
                    return 0
            else:

                return 0 if c > 0 else 1

        if lencs == 0 and c > 0:
            return 0

        if und + c < sumcs:
            return 0

        # not enough symbols for all groups
        if len(p) + c < lencs + sumcs - 1:
            return 0

        if p[0] == '?':
            if lencs > 0:
                if c > 0:
                    if cs[0] == c:
                        return _check(p[1:], cs[1:], 0, path + ".", sumcs - c, und - 1) # choose .
                    elif cs[0] > c:
                        return _check(p[1:], cs, c + 1, path + "#", sumcs, und - 1) # choose #
                    else:
                        return 0
                else:
                    return _check(p[1:], cs, 0, path + ".", sumcs, und - 1) + _check(p[1:], cs, 1, path + "#", sumcs, und - 1)
            else:
                if c > 0:
                    return 0
                else:
                    return _check(p[1:], cs, 0, path + ".", sumcs, und - 1)

        if p[0] == '#':
            return _check(p[1:], cs, c + 1, path + "#", sumcs, und - 1)

        if c > 0 and (lencs == 0 or c != cs[0]):
            return 0

        if c > 0 and lencs > 0 and c == cs[0]:
            return _check(p[1:], cs[1:], 0, path + ".", sumcs - c, und)

        return _check(p[1:], cs, 0, path + ".", sumcs, und)

    return check(p, cs, 0, "", sum(cs), sum([0 if x == '.' else 1 for x in p]))

print(sum([cnt(l) for l in ls]))


