#!/usr/bin/python3

import sys

ls = [l for l in sys.stdin]

g = [[l.strip() for l in g.split("\n") if l != ""] for g in "".join(ls).split("\n\n")]

def reflections(ls):
    def check_lines(ls):

        for i in range(0, len(ls) - 1):
            ok = True
            sf = False
            for j in range(0, len(ls)):
                if i - j < 0 or i + 1 + j >= len(ls):
                    continue
                diff = sum([1 if ls[i - j][k] != ls[i + 1 + j][k] else 0 for k in range(0, len(ls[i - j]))])
                ok = ok and (ls[i - j] == ls[i + 1 + j] or (not sf and diff == 1))
                if diff == 1:
                    sf = True
            if sf and ok:
                return i + 1
        return 0

    return 100 * check_lines(ls) + check_lines(list(zip(*ls)))

print(sum([reflections(ls) for ls in g]))


