#!/usr/bin/python3 

import sys

lns = [l.strip() for l in sys.stdin]

l = "".join([("0000{0:b}".format(int(c, 16)))[-4:] for c in lns[0]])

print(l)

def take(bits, n):
    print(f"taking {n} bits: '{bits[0:n]}', returning '{int(bits[0:n], 2)}'")
    return (int(bits[0:n], 2), bits[n:])


def parse(bits):
    (ver, bits) = take(bits, 3)
    (typ, bits) = take(bits, 3)
    

    if typ == 4:
        n = 0
        (b, bits) = take(bits, 5)
        while b > 15:
            n *= 16
            n += (b % 16)
            (b, bits) = take(bits, 5)
        n *= 16
        n += (b % 16)

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
    print(tree)
    if tree[1] == 4:
        return tree[0]

    return sum([sumver(t) for t in tree[2]]) + tree[0]

print(sumver(tree))

def run(tree):
    if tree[1] == 4:
        return tree[2]
    subs = [run(t) for t in tree[2]]
    if tree[1] == 0:
        return sum(subs)
    if tree[1] == 1:
        p = 1
        for x in subs:
            p *= x
        return p
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
