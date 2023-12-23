#!/usr/bin/python3

import sys
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]


g = {}

X = len(ls[0])
Y = len(ls)

dirs = {
        '>': (1, 0),
        '<': (-1, 0),
        'v': (0, 1),
        '^': (0, -1)
}


S = (ls[0].index('.'), 0)
E = (ls[-1].index('.'), Y - 1)

p = []

p.append(S)
p.append(E)
for y in range(1, Y - 1):
    for x in range(1, X - 1):
        if ls[y][x] != '#':
            d = sum([1 if ls[y + dy][x + dx] != '#' else 0 for (dx, dy) in dirs.values()])
            if d > 2:
                p.append((x, y))

print(p)
print(len(p))

for y in range(0, Y):
    for x in range(0, X):
        g[x, y] = ls[y][x]

def dists(a):
    q = PriorityQueue()
    ds = {}

    q.put((0, a))

    out = {}

    while not q.empty():
        (d, (x, y)) = q.get()

        if (x, y) not in g or g[x, y] == '#' or ((x, y) in ds and ds[x, y] <= d):
            continue

        ds[x, y] = d

        if (x, y) in p and (x, y) != a:
            out[(x, y)] = ds[x, y]
        else:
            for d_ in dirs.values():
                q.put((d + 1, (x + d_[0], y + d_[1])))

    return out

dp = {}
keyset = {}
for i in range(0, len(p)):
    dp[p[i]] = dists(p[i])
    keyset[p[i]] = set(dp[p[i]].keys())
    dp[p[i]] = { k: dp[p[i]][k] for k in sorted(dp[p[i]].keys(), key = lambda x: -dp[p[i]][x]) }


eir_cache = {}
def end_is_reachable(s, seen):
    k = str(s) + str(seen)
    if k in eir_cache:
        return eir_cache[k]
    if E in s:
        eir_cache[k] = True
        return True
    if len(s) == 0:
        eir_cache[k] = False
        return False
    n = set.union(*[keyset[t] for t in s]) - seen
    return end_is_reachable(n, seen | n)

max_path = None
max_len = 0

cache = {}
def longest(a, dist, seen, path):
    global max_path, max_len
    if a == E:
        if dist > max_len:
            max_path = path
            max_len = dist
            print("found", dist)
        return dist

    k = str(a) + str(sorted(seen))

    if k in cache and cache[k] >= dist:
        return -1
    else:
        cache[k] = dist

    if len(keyset[a] - seen) == 0:
        return -1

    if not end_is_reachable(set([a]), seen):
        return -1

    l = max([longest(b, dist + dp[a][b], seen | set([b]), [*path, b]) for b in dp[a] if b not in seen])
    return l


print(dp)
print(len(dp))
print(sum([len(dp[a]) for a in dp]))
print("finding longest paths from", S, "to", E)
print(longest(S, 0, set(), [S]))

print("graph {")
print(f"\"{S}\" [label = \"S\"]")
print(f"\"{E}\" [label = \"E\"]")
done = set()
for a in dp:
    for b in dp[a]:
        if b not in done:
            pw = 1
            if (b != E and b in max_path and max_path[max_path.index(b) + 1] == a) or (a != E and a in max_path and max_path[max_path.index(a) + 1] == b):
                pw = 3
            print(f"\"{a}\" -- \"{b}\" [label=\"{dp[a][b]}\", penwidth={pw}]")
    done.add(a)
print("}")
