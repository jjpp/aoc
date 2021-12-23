#!/usr/bin/python3

import sys
from queue import PriorityQueue

lns = [l.strip() for l in sys.stdin]

print(lns)

s = '.......' + lns[2][3] + lns[3][1] + lns[2][5] + lns[3][3] + lns[2][7] + lns[3][5] + lns[2][9] + lns[3][7]
FINAL = '.......AABBCCDD'

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
        sr = (i - 7) // 2
        if sr == ord(s[i]) - ord('A'):
            if (i - 7) % 2 == 1:
                return CANNOT
            if s[i + 1] == s[i]:
                return CANNOT

        if (i - 7) % 2 == 1:
            if s[i - 1] != '.':
                return CANNOT

        e = (i - 7) // 2 + 1.5
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


        price = sc[s[i]] * ((1 + (i - 7) % 2) + abs((2 + ((i - 7) // 2) * 2) - dhw[j]))

        return (True, price, swap(s, i, j))
            
    # hallway to room:
    if i < 7 and j >= 7:

        if (j - 7) % 2 == 1:
            if s[j - 1] != '.':
                return CANNOT

        tr = (j - 7) // 2
        if tr != ord(s[i]) - ord('A'):
            return CANNOT
        if (j - 7) % 2 == 0 and s[j + 1] != s[i]:
            return CANNOT

        e = (j - 7) // 2 + 1.5
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

        price = sc[s[i]] * ((1 + (j - 7) % 2) + abs((2 + ((j - 7) // 2) * 2) - dhw[i]))

        return (True, price, swap(s, i, j))

    # room to room
    if i >= 7 and j >= 7:
        sr = (i - 7) // 2
        if sr == ord(s[i]) - ord('A'):
            if (i - 7) % 2 == 1:
                return CANNOT
            if s[i + 1] == s[i]:
                return CANNOT

        tr = (j - 7) // 2
        if tr != ord(s[i]) - ord('A'):
            return CANNOT
        if (j - 7) % 2 == 0 and s[j + 1] != s[i]:
            return CANNOT

        if (i - 7) % 2 == 1:
            if s[i - 1] != '.':
                return CANNOT

        if (j - 7) % 2 == 1:
            if s[j - 1] != '.':
                return CANNOT
        else:
            if s[j + 1] != s[i]:
                return CANNOT

        e1 = (i - 7) // 2 + 2
        e2 = (j - 7) // 2 + 2

        if e1 == e2:
            return CANNOT

        for k in range(min(e1, e2), max(e1, e2)):
            if s[k] != '.':
                return CANNOT

        price = sc[s[i]] * (
                (1 + (i - 7) % 2) +
                (1 + (j - 7) % 2) +
                abs((2 + ((j - 7) // 2) * 2) - (2 + ((i - 7) // 2) * 2)))

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

