#!/usr/bin/python3

import sys
from queue import PriorityQueue

lns = [l.strip() for l in sys.stdin]

print(lns)

s = '.......' + lns[2][3] + 'DD' + lns[3][1] + lns[2][5] + 'CB' + lns[3][3] + lns[2][7] + 'BA' + lns[3][5] + lns[2][9] + 'AC' + lns[3][7]
FINAL = '.......AAAABBBBCCCCDDDD'

sc = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
dhw = [ 0, 1, 3, 5, 7, 9, 10 ]

ss = { s : 0 }
q = PriorityQueue()
q.put((0, s))

def swap(s, i, j):
    (i, j) = (min(i,j), max(i,j))
    return s[0:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

def check(s, i, j):
    CANNOT = (False, None, None)

    # hallway to hallway
    if i < 7 and j < 7:
        return CANNOT

    # room to hallway:
    if i >= 7 and j < 7:
        sr = (i - 7) // 4
#        print(f"room to hw, before: '{s[7 + sr * 4:i]}' vs '{'.' * ((i - 7) % 4)}'")
        if s[7 + sr * 4:i] != '.' * ((i - 7) % 4):
            return CANNOT

        if sr == ord(s[i]) - ord('A'):
#            print(f"room to hw, after: '{s[i + 1:11 + sr * 4]}' vs '{s[i] * (3 - (i - 7) % 4)}'")
            if s[i + 1:11 + sr * 4] == s[i] * (3 - (i - 7) % 4):
                return CANNOT
                
        e = (i - 7) // 4 + 1.5
        if e < j:
            k = j - 1
            while k > e:
                if s[k] != '.':
                    return CANNOT
                k -= 1
        else:
            k = j + 1
            while k < e:
                if s[k] != '.':
                    return CANNOT
                k += 1


        price = sc[s[i]] * ((1 + (i - 7) % 4) + abs((2 + ((i - 7) // 4) * 2) - dhw[j]))

        return (True, price, swap(s, i, j))
            
    # hallway to room:
    if i < 7 and j >= 7:
        tr = (j - 7) // 4
        if tr != ord(s[i]) - ord('A'):
            return CANNOT

        #print(f"hw to room, before '{s[7 + tr * 4:j]}' vs '{'.' * ((j - 7) % 4)}'")
        if s[7 + tr * 4:j] != '.' * ((j - 7) % 4):
            return CANNOT

        #print(f"hw to room, after '{s[j + 1:11 + tr * 4]}' vs '{s[i] * (3 - (j - 7) % 4)}'")
        if s[j + 1:11 + tr * 4] != s[i] * (3 - (j - 7) % 4):
            return CANNOT

        e = (j - 7) // 4 + 1.5
        if e < i:
            k = i - 1
            while k > e:
                if s[k] != '.':
                    return CANNOT
                k -= 1
        else:
            k = i + 1
            while k < e:
                if s[k] != '.':
                    return CANNOT
                k += 1

        price = sc[s[i]] * ((1 + (j - 7) % 4) + abs((2 + ((j - 7) // 4) * 2) - dhw[i]))

        return (True, price, swap(s, i, j))

    # room to room
    if i >= 7 and j >= 7:
        sr = (i - 7) // 4
#        print(f"room to hw, before: '{s[7 + sr * 4:i]}' vs '{'.' * ((i - 7) % 4)}'")
        if s[7 + sr * 4:i] != '.' * ((i - 7) % 4):
            return CANNOT

        if sr == ord(s[i]) - ord('A'):
#            print(f"room to hw, after: '{s[i + 1:11 + sr * 4]}' vs '{s[i] * (3 - (i - 7) % 4)}'")
            if s[i + 1:11 + sr * 4] == s[i] * (3 - (i - 7) % 4):
                return CANNOT

        tr = (j - 7) // 4
        if tr != ord(s[i]) - ord('A'):
            return CANNOT

        #print(f"hw to room, before '{s[7 + tr * 4:j]}' vs '{'.' * ((j - 7) % 4)}'")
        if s[7 + tr * 4:j] != '.' * ((j - 7) % 4):
            return CANNOT

        #print(f"hw to room, after '{s[j + 1:11 + tr * 4]}' vs '{s[i] * (3 - (j - 7) % 4)}'")
        if s[j + 1:11 + tr * 4] != s[i] * (3 - (j - 7) % 4):
            return CANNOT

        e1 = (i - 7) // 4 + 2
        e2 = (j - 7) // 4 + 2

        if e1 == e2:
            return CANNOT

        for k in range(min(e1, e2), max(e1, e2)):
            if s[k] != '.':
                return CANNOT

        price = sc[s[i]] * (
                (1 + (i - 7) % 4) +
                (1 + (j - 7) % 4) +
                abs((2 + ((j - 7) // 4) * 2) - (2 + ((i - 7) // 4) * 2)))

        return (True, price, swap(s, i, j))

def p1():
    while not q.empty():
        (score, s) = q.get()
        print(f"checking {s} with {score}")
        if s in ss and score > ss[s]:
            print(f"skipping, {score} > {ss[s]}")
            continue
        for (i, f) in enumerate(s):
            if f == '.':
                continue
            for (j, t) in enumerate(s):
                if t != '.':
                    continue
                (can_move, price, new) = check(s, i, j)
                if can_move:
                    print(f"{s} -> {new}, {price} {f}@{i} -> {j} ({len(ss)}, {q.qsize()}, {ss[new] if new in ss else None})")
                    if new not in ss or (score + price) < ss[new]:
                        print("adding to queue")
                        ss[new] = score + price
                        q.put((score + price, new))

    return ss[FINAL]


print(p1())

