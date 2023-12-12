#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

def cnt(l):
    (p, cs) = l.split()
    cs = [int(c) for c in cs.split(',')]

    def check(p, cs, c, path):
#        print(f"checking {path} {p}, {cs}, {c}")
        if p == "":
            if len(cs) > 1:
                return 0
            elif len(cs) == 1:
                if cs[0] == c:
#                    print(f"F: {path}")
                    return 1
                else:
                    return 0
            else:
 #               if c == 0:
 #                   print(f"F: {path}")

                return 0 if c > 0 else 1

        if len(cs) == 0 and c > 0:
            return 0

        if p[0] == '?':
            if len(cs) > 0:
                if c > 0:
                    if cs[0] == c:
                        return check(p[1:], cs[1:], 0, path + ".") # choose .
                    elif cs[0] > c:
                        return check(p[1:], cs, c + 1, path + "#") # choose #
                    else:
                        return 0
                else:
                    return check(p[1:], cs, 0, path + ".") + check(p[1:], cs, 1, path + "#")
            else:
                if c > 0:
                    return 0
                else:
                    return check(p[1:], cs, 0, path + ".")

        if p[0] == '#':
            return check(p[1:], cs, c + 1, path + "#")

        if c > 0 and (len(cs) == 0 or c != cs[0]):
            return 0

        if c > 0 and len(cs) > 0 and c == cs[0]:
            return check(p[1:], cs[1:], 0, path + ".")

        return check(p[1:], cs, 0, path + ".")

    return check(p, cs, 0, "")


print(sum([cnt(l) for l in ls]))


