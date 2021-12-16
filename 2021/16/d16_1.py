#!/usr/bin/python3 

import sys
import functools

lns = [l.strip() for l in sys.stdin]

l = "".join([f"{int(c, 16):04b}" for c in lns[0]])

def take(bits, n):
    return (int(bits[0:n], 2), bits[n:])


def parse(bits):
    (ver, bits) = take(bits, 3)
    (typ, bits) = take(bits, 3)
    

    if typ == 4:
        n = 0
        while True:
            (b, bits) = take(bits, 5)
            n *= 16
            n += (b % 16)
            if b < 16:
                break

        return ((ver, typ, n), bits)

    (lti, bits) = take(bits, 1)

    subpts = []

    if lti == 0:
        (l, bits) = take(bits, 15)
        subbits = bits[0:l]
        bits = bits[l:]
        while len(subbits) > 0:
            (subpt, subbits) = parse(subbits)
            subpts.append(subpt)
    else:
        (l, bits) = take(bits, 11)
        for i in range(l):
            (subpt, bits) = parse(bits)
            subpts.append(subpt)
    
    return ((ver, typ, subpts), bits)

(tree, bits) = parse(l)

def sumver(tree):
    return tree[0] + (0 if tree[1] == 4 else sum([sumver(t) for t in tree[2]]))

print(sumver(tree))

def run(tree):
    if tree[1] == 4:
        return tree[2]
    subs = [run(t) for t in tree[2]]
    if tree[1] == 0:
        return sum(subs)
    if tree[1] == 1:
        return functools.reduce(lambda a, x: x*a, subs)
    if tree[1] == 2:
        return min(subs)
    if tree[1] == 3:
        return max(subs)
    if tree[1] == 5:
        return 1 if subs[0] > subs[1] else 0
    if tree[1] == 6:
        return 1 if subs[0] < subs[1] else 0
    if tree[1] == 7:
        return 1 if subs[0] == subs[1] else 0

    raise "Unknown type " + tree

print(run(tree))

