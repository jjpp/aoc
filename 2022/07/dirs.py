#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

dirs = {}
sizes = {}

pwd = []

def du(pwd):
    cwd = "/".join(pwd)
    if not cwd in dirs:
        print(f"Unknown dir {cwd}")
        return 0

    total = 0
    for n, i in dirs[cwd].items():
        if i[0] == 'dir':
            i[1] = du(pwd + [n])
        total += i[1]
    sizes[cwd] = total
    return total


while len(ls) > 0:
    c = ls.pop(0).split(' ')

    if c[0] == '$':
        if c[1] == 'cd':
            if c[2] == '/':
                pwd = []
            elif c[2] == '..':
                pwd.pop()
            else:
                pwd.append(c[2])
        elif c[1] == 'ls':
            cwd = "/".join(pwd)
            dirs[cwd] = {}
            while len(ls) > 0 and ls[0][0] != '$':
                [size, name] = ls.pop(0).split(' ')
                if size == 'dir':
                    type_ = 'dir'
                    size = None
                else:
                    type_ = 'file'
                    size = int(size)
                dirs[cwd][name] = [type_, size]
    else:
        print(f"Something is fishy: {c[0]} {c[1]} {arg}")



used = du([])
need = 30000000
total = 70000000

print(sum([s for s in sizes.values() if s < 100000]))

ss = list(sorted(sizes, key = lambda x: sizes[x]))

while len(ss) > 0:
    if total - used + sizes[ss[0]] < need:
        ss.pop(0)
    else:
        break

if len(ss) > 0:
    print(sizes[ss[0]])
else:
    print("This should not happen")


