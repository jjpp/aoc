#!/usr/bin/python3

# interactive version, used to import into
# python REPL and play with different inputs

import sys
import re


ls = """Register A: 59397658
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0
""".split("\n")

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

r = [nums(ls[0])[0], nums(ls[1])[0], nums(ls[2])[0]]
orig_r = [*r]
code = nums(ls[4])
ip = 0
out = []

def combo(p):
    if p < 4:
        return p
    if 4 <= p < 7:
        return r[p - 4]
    raise ValueError("Illegal combo value")

def step():
    global ip, code, out, r

    if ip >= len(code):
        return False
    
    op = code[ip]
    p = code[ip + 1]
    ip += 2

#    print (op, p, ip, r, out)

    if op == 0: # adv
        r[0] = r[0] // (2 ** combo(p))
    elif op == 1: # bxl
        r[1] = r[1] ^ p
    elif op == 2: # bst
        r[1] = combo(p) % 8 
    elif op == 3: # jnz
        if r[0] != 0:
            if p == ip - 2:
                # halt by infinite loop
                return False
            ip = p
    elif op == 4: # bxc
        r[1] = r[1] ^ r[2]
    elif op == 5: # out
        out.append(combo(p) % 8)
    elif op == 6: # bdv
        r[1] = r[0] // (2 ** combo(p))
    elif op == 7: # cdv
        r[2] = r[0] // (2 ** combo(p))

    return True

def run(a):
    global orig_r, r, ip, code, out

    steps = 0
    r = orig_r
    r[0] = a
    out = []
    ip = 0

#    print("run ", a)

    while steps < 10000000 and len(out) <= len(code):
        if not step():
            break
        steps += 1

#    print(code)
#    print(code == out)
    return out

def ca(aa):
    o = 0
    for x in aa:
        o = 8*o + x
    return o

def r(aa):
    o = ca(aa)
    print(o)
    print(run(o))

def tabel():
    for a in range(8):
        for b in range(8):
            for c in range(8):
                print(c, b, a, run(a*64 + b*8 + c))

