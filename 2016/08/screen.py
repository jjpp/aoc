#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

max_x = 50
max_y = 6

#max_x = 8
#max_y = 3

s = [[" " for i in range(0, max_x)] for j in range(0, max_y)]

for l in ls:
    print(l)
    cmd = l.split()
    if cmd[0] == "rect":
        (x, y) = cmd[1].split('x')
        print(x, y)
        for i in range(0, int(y)):
            for j in range(0, int(x)):
                s[i][j] = "#"

    elif cmd[0] == "rotate":
        if cmd[1] == "row":
            a = int(cmd[2][2:])
            b = int(cmd[4]) % max_x

            s[a] = s[a][max_x - b:] + s[a][:max_x - b]

        else:
            a = int(cmd[2][2:])
            b = int(cmd[4]) % max_y

            row = [s[i][a] for i in range(0, max_y)]
            for i in range(0, max_y):
                s[i][a] = row[(max_y + i - b) % max_y]

    for j in range(0, max_y):
        print("".join(s[j]))

count = sum([1 if c == "#" else 0 for c in "".join(["".join(l) for l in s])])

print(count)
