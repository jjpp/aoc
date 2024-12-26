#!/usr/bin/python3

# part 1

import sys
import re

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

rs = [nums(l) for l in ls]
X = 101
Y = 103

def iterate(rs):
    return [((r[0] + r[2] + X) % X, (r[1] + r[3] + Y) % Y, r[2], r[3]) for r in rs]
    

def sec(rs):
    q1 = len([r for r in rs if r[0] < int(X/2) and r[1] < int(Y/2)])
    q2 = len([r for r in rs if r[0] > int(X/2) and r[1] < int(Y/2)])
    q3 = len([r for r in rs if r[0] < int(X/2) and r[1] > int(Y/2)])
    q4 = len([r for r in rs if r[0] > int(X/2) and r[1] > int(Y/2)])
    # print(q1,q2,q3,q4)
    return q1*q2*q3*q4

for _ in range(100):
    rs = iterate(rs)

print(sec(rs))

