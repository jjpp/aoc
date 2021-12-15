#!/usr/bin/python3

import sys

ls = ["." + l.strip() + "." for l in sys.stdin]
ls.insert(0, "." * len(ls[0]))
ls.append(ls[0])

def is_corner(x, y):
    return (x == 1 and y == 1) or (x == 1 and y == len(ls) - 2) or \
           (x == len(ls[0]) - 2 and y == 1) or (x == len(ls[0]) - 2 and y == len(ls) - 2)

def iterate(ls):
    os = [ls[0]]

    for row in range(1, len(ls) - 1):
        o = ""
        for col in range(1, len(ls[row])-1):
            ns = ls[row - 1][col-1:col+2] + ls[row][col-1] + ls[row][col+1] + ls[row + 1][col-1:col+2]
            on = sum([1 if c == '#' else 0 for c in 
                    (ls[row - 1][col-1:col+2] + ls[row][col-1] + ls[row][col+1] + ls[row + 1][col-1:col+2])])
#            print(row, col, on, ls[row][col], ns)
            o += "#" if is_corner(col, row) or (ls[row][col] == '#' and (on == 2 or on == 3)) or (ls[row][col] == "." and on == 3) else "."
        os.append("." + o + ".")

    os.append(ls[0])

    print("\n".join(os))
    print("------")

    return os

#print("\n".join(ls))
#print("------")

for i in range(0, 100):
    ls = iterate(ls)

count = sum([1 if c == "#" else 0 for c in "".join(ls)])
print(count)
