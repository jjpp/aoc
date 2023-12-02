#!/usr/bin/python3

import sys
from queue import PriorityQueue
from itertools import combinations

#ls = [l.strip() for l in sys.stdin]

# The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
# The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
# The third floor contains a thulium-compatible microchip.
# The fourth floor contains nothing relevant.

state = [1, set(['sg', 'sm', 'pg', 'pm']), set(['tg', 'rg', 'rm', 'cg', 'cm']), set(['tm']), set()]
state = [1, set(['sg', 'sm', 'pg', 'pm']), set(['tg', 'rg', 'rm', 'cg', 'cm']), set(['tm']), set()]
state = [1, set(['eg', 'em', 'dg', 'dm', 'sg', 'sm', 'pg', 'pm']), set(['tg', 'rg', 'rm', 'cg', 'cm']), set(['tm']), set()]
#state = [1, set(['hm', 'lm']), set(['hg']), set(['lg']), set()]

state0 = str(state)

pq = PriorityQueue()
pq.put((len(state[1] | state[2] | state[3]), 0, state0))

seen = set()

def sustainable(s):
    for x in s:
        if x[1] == 'm' and x[0] + 'g' not in s:
            return False
    return True

while not pq.empty():
    (_, d, s_) = pq.get()
    if s_ in seen:
        continue
    seen.add(s_)
    print(f"Checking: after {d} steps: {s_}")
    s = eval(s_)

    if len(s[1]) + len(s[2]) + len(s[3]) == 0:
        print(d)
        break
    
    for d_ in [-1, 1]:
        if s[0] + d_ < 1 or s[0] + d_ > 4:
            continue

        dest = s[0] + d_
        
        for b_ in [1, 2]:
            for b in combinations(s[s[0]], b_):
                if sustainable(s[dest].union(b)):
                    new_state = [dest] + [ s[i].union(b) if i == dest else s[i] - set(b) if i == s[0] else s[i] for i in range(1, 5) ]
                    pq.put((len(new_state[1] | new_state[2] | new_state[3]), d + 1, str(new_state)))
                    


