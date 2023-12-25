#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

g = {}
e = {}

for l in ls:
    ks = l.split()
    ks[0] = ks[0][0:-1]

    if ks[0] not in g:
        g[ks[0]] = {}

    for k in ks[1:]:
        e[ks[0], k] = 1
        e[k, ks[0]] = 2
        if k not in g:
            g[k] = {}
        g[ks[0]][k] = 1
        g[k][ks[0]] = 2

def print_graph():
    print("graph {")
    for k in g:
        for l in g[k]:
            if g[k][l] == 1:
                print(k, "--", l)
    print("}")

# solution: print out the graph as graphviz source,
# visualize it and find the 3 obvious edges visually.
# then let the code count nodes

# print_graph()

# edges are:
#  vtt-fht czs-tdk bbg-kbr

def delete(a, b):
    if (a, b) in e:
        del e[a, b]
    if (b, a) in e:
        del e[b, a]
    del g[a][b]
    del g[b][a]

delete('vtt', 'fht')
delete('czs', 'tdk')
delete('bbg', 'kbr')

seen = set()

q = []
q.append('vtt')
while len(q) > 0:
    n = q.pop()
    if n in seen:
        continue
    seen.add(n)
    for n2 in g[n]:
        q.append(n2)

print(len(seen) * (len(g.keys()) - len(seen)))

