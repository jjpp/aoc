#!/usr/bin/python3

import sys

ls = [l for l in sys.stdin]

g = [[l.strip() for l in g.split("\n") if l != ""] for g in "".join(ls).split("\n\n")]

def reflections(ls):
    def check_lines(ls):
        for i in range(0, len(ls) - 1):
            ok = True
            for j in range(0, len(ls)):
                ok = ok and (i - j < 0 or i + 1 + j >= len(ls) or ls[i - j] == ls[i + 1 + j])
            if ok:
                return i + 1
        return 0

    return 100 * check_lines(ls) + check_lines(list(zip(*ls)))

print(sum([reflections(ls) for ls in g]))


