#!/usr/bin/python3

# part 2

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
    
def print_map(rs, s, teststr = "X"):
    rm = set([(r[0], r[1]) for r in rs])
    os = []
    c = False
    for y in range(Y):
        o = ""
        for x in range(X):
            o += "X" if (x, y) in rm else " "
        c = c or teststr in o
        os.append(o)

    if c:
        for o in os:
            print(o)
        print("step ", s)
        print()

    return c

s = 0

# initial solution: 
# * print out the map after each iteration, together with the iteration number
# * pipe it to less and visually scan for trees
# * realise, the tree likely has many robots in a row, search for "XXXXXXX" or
#   something like that in the stream of maps
# * soon enough, a picture of a tree appears.. submit the number of iteration.
while True:
    rs = iterate(rs)
    s += 1
    if print_map(rs, s, "XXXXXXXXXXXXXXXXXXXXX"):
        break

