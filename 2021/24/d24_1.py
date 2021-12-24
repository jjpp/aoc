#!/usr/bin/python3

import sys

lns = [l.strip() for l in sys.stdin]

fun = {
        'add': lambda r, a, b: r[a] + val(r, b),
        'mul': lambda r, a, b: r[a] * val(r, b),
        'div': lambda r, a, b: r[a] // val(r, b),
        'mod': lambda r, a, b: r[a] % val(r, b),
        'eql': lambda r, a, b: int(r[a] == val(r, b))
}

def val(r, b):
    if b in "xyzw":
        return r[b]
    return int(b)

def parse(lns):
    return [l.split(' ') for l in lns]

def pp(z):
    o = ""
    while z > 0:
        o += chr(z % 26 + ord('A'))
        z //= 26
    return o

def run(code, param):
    regs = { 'x': 0, 'y': 0, 'z': 0, 'w': 0 }
    ip = 0
    for c in code:
        if c[0] == 'inp':
            regs[c[1]] = int(param[ip])
            ip += 1
            #print(regs, ip - 1)
        else:
            regs[c[1]] = fun[c[0]](regs, c[1], c[2])
        #print(f"{c[1]} = {regs[c[1]]} ({c}) {regs}")
        #if c[1] == 'z':
            #print(pp(regs['z']))

    print(regs)
    return regs['z'] == 0

code = parse(lns)

run(code, '92915979999498')
run(code, '21611513911181')

