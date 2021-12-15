#!/usr/bin/python3

import sys

rs = {}
ts = set()
m = ""

class terminal(str):
    def __str__(self):
        return "terminal(" + str(self) + ")"
    ...

for l in sys.stdin:
    l = l.strip()
    if " => " in l:
        [a, _, b] = l.split(' ')
        if not a in rs:
            rs[a] = set()
        rs[a] |= set([b])
    elif len(l) > 0:
        m = l

for (k, vs) in rs.items():
    vs_ = []
    if False and k != "e":
        vs_ = [[terminal(k)]]
        ts |= { k }
    for v in vs: 
        o = []
        while len(v) > 0:
            i = min([v.index(k_) for k_ in rs.keys() if k_ in v] + [len(v) + 1])
            if i > len(v):
                o.append(terminal(v))
                v = ""
                continue
            if i > 0:
                o.append(terminal(v[0:i]))
                v = v[i:]
            k_ = [k_ for k_ in rs.keys() if v.startswith(k_)][0]
            o.append(k_)
            v = v[len(k_):]
        vs_.append(o)
        ts |= { *o }
    rs[k] = vs_

rs["e'"] = [["e"]]

print(rs)
print(ts)

lx = [None]
while len(m) > 0:
    w = [w for w in ts if m.startswith(w)][0]
    lx.append(w)
    m = m[len(w):]

print(lx)

def add_state(k, name, prod, pos, startsat):
    new_state = [name, prod, pos, startsat]
    if not new_state in s[k]:
        s[k].append(new_state)
        print("for", k, "added", s[k][-1])
    else:
        print("skipped duplicate", new_state, "for", k)

def add_consumed(k, state):
    add_state(k, state[0], state[1], state[2] + 1, state[3])


s = [[] for i in range(0, len(lx))]
add_state(0, "e'", ["e"], 0, 0)

def completed(state):
    return state[2] >= len(state[1])

def next_of(state):
    if completed(state):
        return None
    return state[1][state[2]]

def predict(next_elem, k):
    for r in rs[next_elem]:
        print("predict", k)
        add_state(k, next_elem, r, 0, k)

def scan(k):
    term = lx[k + 1] if k + 1 < len(lx) else None
    for s_ in s[k]:
        if not completed(s_) and next_of(s_) == term:
            print("scan",k)
            add_consumed(k + 1, s_)

def complete(state, k):
    for s_ in s[state[3]]:
        if next_of(s_) == state[0]:
            print("complete",state,k)
            add_consumed(k, s_)

for k in range(0, len(s)):
    for state in s[k]:
        if not completed(state):
            next_elem = next_of(state)
            if not isinstance(next_elem, terminal):
                predict(next_elem, k)
            else:
                scan(k)
        else:
            complete(state, k)

root = None
for s_ in s[-1]:
    if s_[0] == "e'" and completed(s_):
        print("ok:", s_)
        root = s_

def build_trees(state, k):
    print("build_trees", state, k)
    return build_trees_helper([], state, len(state[1]) - 1, k)

def build_trees_helper(children, state, rule_index, end_column):
    while rule_index >= 0:
        rule = state[1][rule_index]
        if not isinstance(rule, terminal):
            break
        rule_index -= 1

    if rule_index < 0:
        print("returning",[state, children])
        return [[state, children]]
    elif rule_index == 0:
        start_column = state[3]
    else:
        start_column = None

    print("b_t_h", state, rule, rule_index, start_column, end_column)
    
    outputs = []
    for st in s[end_column]:
        print("  bth", st)
        if st is state:
            print("    is state")
            break
        if st is state or not completed(st) or st[0] != rule:
            print("    not relevant rule")
            continue
        if start_column is not None and st[3] != start_column:
            print("    not matching start col")
            continue
        for sub_tree in build_trees(st, end_column):
            print("    scanning subtrees", sub_tree)
            for node in build_trees_helper([sub_tree] + children, state, rule_index - 1, st[3]):
                print("appending node", node
                outputs.append(node)
    return outputs


print(build_trees(root, len(s) - 1))

