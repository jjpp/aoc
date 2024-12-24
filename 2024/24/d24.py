#!/usr/bin/python3

# initial scratchpad-attempt on top of p1
# used this to see where there is a mismatch
# and fix the input until all swaps were 
# found (manually)..
# eventually implemented an automated solution
# as d24_2.py

import sys, re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

ovs = {}
vs = {}
syms = {}
rsyms = {}
m = {}

for l in range(ls.index('')):
    (var, val) = ls[l].split(': ')
    ovs[var] = vs[var] = int(val)

ops = {
        'XOR': lambda a, b: lambda: g(a) ^ g(b),
        'OR':  lambda a, b: lambda: g(a) | g(b),
        'AND': lambda a, b: lambda: g(a) & g(b),
}

def g(v):
    if not isinstance(vs[v], int):
        vs[v] = vs[v]()
    return vs[v]

    
for l in range(ls.index('') + 1, len(ls)):
    (a, op, b, _, r) = ls[l].split(' ')
    ovs[r] = vs[r] = ops[op](a, b)
    if a > b:
        (a, b) = (b, a)
    syms[r] = (a, op, b)
    rsyms[a, op, b] = r
    m[a] = a
    m[b] = b
    m[r] = r

print(len(m))


# z_0 = x_0 xor y_0
# c_0 = x_0 and y_0

# s_n = x_n xor y_n 
# z_n = s_n xor c_n
# d_n = x_n and y_n
# e_n = s_n and c_n
# c_n+1 = e_n or d_n

# x + y + c 
# s = x xor y
# d = x and y
# z = s xor c
# e = s and c
# c' = d or e

# z_last = c_n-1

zs = sorted([x for x in vs.keys() if x[0] == 'z'])


def find(a, op, b):
    if (m[a], op, m[b]) in rsyms:
        return rsyms[m[a], op, m[b]]

    if (m[b], op, m[a]) in rsyms:
        return rsyms[m[b], op, m[a]]

    print("cannot find", a, op, b)
    print(a, '=', m[a])
    print(b, '=', m[b])

    for (a_, op_, b_) in rsyms:
        if (m[a] == a_ or m[b] == a_ or m[a] == b_ or m[b] == b_) and op == op_:
            print("  ", a_, op_, b_, '->', rsyms[a_, op_, b_])

    return 'xxx'

def setm(p, w, n):
    print(f"Setting {p}{w} to {n} (prev: {m.get(p + w, None)})")
    if re.fullmatch("[xycdesz][0-9][0-9]", m.get(p + w, 'xxx')) and p+w != m[p+w]:
        print("need to swap ", p+w, " and ", m[p+w])
    if re.fullmatch("[xycdesz][0-9][0-9]", n) and p+w != n:
        print("need to swap ", p+w, " and ", n)
    m[n] = p + w
    m[p + w] = n

z00 = find('x00', 'XOR', 'y00')
setm('z', '00', z00)

last = zs[-1][1:]
first = '00'

print("last: ", last)
for w in [z[1:] for z in zs[:-1]]:
    w_ = str("00" + str(int(w) + 1))[-2:]
    print(f"[{w}], [{w_}]")

    s = find('x' + w, 'XOR', 'y' + w)
    setm('s' if w != first else 'z', w, s)

    if w == first:
        c = find('x' + w, 'AND', 'y' + w)
        setm('c', w_, c)
    else:
        d = find('x' + w, 'AND', 'y' + w)
        setm('d', w, d)

    if w != last and w != first:
        z = find('s' + w, 'XOR', 'c' + w)
        if z != 'z' + w:
            print("mismatch: ", z, 'z'+w)
        
        e = find('s' + w, 'AND', 'c' + w)
        setm('e', w, e)

        c = find('e' + w, 'OR', 'd' + w)
        setm('c' if w_ != last else 'z', w_, c)


def get(var):
    out = 0
    for z in reversed(sorted([v for v in vs.keys() if v[0] == var])):
        out *= 2
        out += g(z)
    return out

print(get('x'), '+', get('y'), '=', get('z'))
