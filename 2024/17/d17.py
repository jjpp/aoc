#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

r = [nums(ls[0])[0], nums(ls[1])[0], nums(ls[2])[0]]
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

    # print (op, p, ip, r, out)

    if op == 0: # adv
        r[0] = r[0] // (2 ** combo(p))
    elif op == 1: # bxl
        r[1] = r[1] ^ p
    elif op == 2: # bst
        r[1] = combo(p) % 8 
    elif op == 3: # jnz
        if r[0] != 0:
            ip = p
    elif op == 4: # bxc
        r[1] = r[1] ^ r[2]
    elif op == 5: # out
        out.append(str(combo(p) % 8))
    elif op == 6: # bdv
        r[1] = r[0] // (2 ** combo(p))
    elif op == 7: # cdv
        r[2] = r[0] // (2 ** combo(p))

    return True

while True:
    if not step():
        break

# print(r, ip)
print(",".join(out))



