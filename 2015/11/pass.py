#!/usr/bin/python3

p = 'hxbxwxba'

def inc(p, i):
    if i < 0:
        return
    p[i] += 1

    if p[i] > ord('z'):
        p[i] = ord('a')
        inc(p, i - 1)

def fix_iol(p):
    bs = bytes('iol', 'utf-8')
    for i in range(0, 8):
        if p[i] in bs:
            inc(p, i)
            for j in range(i + 1, 8):
                p[j] = ord('a')
            return


def has_triple(p):
    for i in range(2, 8):
        if p[i - 2] + 1 == p[i - 1] and p[i - 1] + 1 == p[i]:
            return True

    return False

def has_pairs(p):
    fp = None
    for i in range(0, 7):
        if p[i] != p[i+1]:
            continue
        if fp == None:
            fp = i
        elif i > fp + 1:
            return True
    return False



def nextpass(p):
    p = [ord(c) for c in p]

    print(p)

    while True:
        inc(p, 7)
        fix_iol(p)
        
        if not has_triple(p):
            continue

        if not has_pairs(p):
            continue

        break

    return "".join([chr(c) for c in p])


p = nextpass(p)
print(p)
print(nextpass(p))

