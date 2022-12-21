#!/usr/bin/python3

import sys
import re

ls = [l.strip() for l in sys.stdin]


m = {}
t = {}

for l in ls:
    n, v = l.split(': ')
    d = v.split(' ')
    if len(d) == 1:
        m[n] = v
    else:
        m[n] = d

m['humn'] = 'x'
m['root'][1] = '=='

while isinstance(m['root'], list):
    for k in m:
        if isinstance(m[k], list):
            if not(isinstance(m[m[k][0]], list)) and not(isinstance(m[m[k][2]], list)):
                v = "(" +str(m[m[k][0]]) + m[k][1] + str(m[m[k][2]]) + ")"
                if 'x' not in v:
                    v = str(int(eval(v)))
                    t[k] = v
                else:
                    a = t[m[k][0]] if m[k][0] in t else m[m[k][0]]
                    b = t[m[k][2]] if m[k][2] in t else m[m[k][2]]

                    t[k] = [a, m[k][1], b]
                m[k] = v


while isinstance(t['root'], list):
    r = t['root']

    if r[0] == 'x' or r[0] == ['x']:
        print(r[2])
        exit(0)

    match r[0]:
        # x is on wrong side, swap them
        case str(a):
            t['root'] = list(reversed(t['root']))

        # x is also a str, make it list 
        case 'x', op, str(b):
            t['root'] = [[['x'], op, b], '==', r[2]]
        case str(a), op, 'x':
            t['root'] = [[a, op, ['x']], '==', r[2]]

        # reduce one elementary step
        case str(a), '/', list(b):
            t['root'] = [b, '==', str(int(a) // int(r[2]))]
        case str(a), '*', list(b):
            t['root'] = [b, '==', str(int(r[2]) // int(a))]
        case str(a), '+', list(b):
            t['root'] = [b, '==', str(int(r[2]) - int(a))]
        case str(a), '-', list(b):
            t['root'] = [b, '==', str(int(a) - int(r[2]))]
        case list(a), '/', str(b):
            t['root'] = [a, '==', str(int(b) * int(r[2]))]
        case list(a), '*', str(b):
            t['root'] = [a, '==', str(int(r[2]) // int(b))]
        case list(a), '+', str(b):
            t['root'] = [a, '==', str(int(r[2]) - int(b))]
        case list(a), '-', str(b):
            t['root'] = [a, '==', str(int(r[2]) + int(b))]

        case _:
            print("should not happen")
            exit(1)



