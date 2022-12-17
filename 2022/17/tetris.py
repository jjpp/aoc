#!/usr/bin/python3

# does give correct answers for test and my input.

import sys

ls = [l.strip() for l in sys.stdin]

ps = list(ls[0])

g = {}
h = 0
cmd_index = 0

blocks = [ ["@@@@"], [".@.", "@@@", ".@."], ["@@@", "..@", "..@"], ["@", "@", "@", "@"], ["@@", "@@"] ]

def fall(b, pc = False):
    global cmd_index
    y = h + 3
    x = 2
    cmd = 0

    def can_move_to(x, y):
        if x < 0 or x + len(b[0]) > 7 or y < 0:
            return False
        if y > h:
            return True
        for r in range(len(b)):
            for c in range(len(b[0])):
                if b[r][c] == '@' and (y + r, x + c) in g:
                    return False
        
        return True

    def put(x, y):
        global h
        for r in range(len(b)):
            for c in range(len(b[0])):
                if b[r][c] == '@':
                    g[(y + r, x + c)] = '#'
                    h = max(h, y + r + 1)

    def print_cave():
        print(cmd_index, cmd, h, x, y)
        for r in reversed(range(h + 2 + len(b))):
            out = f'{r:5}|'
            for c in range(7):
                if (r, c) in g:
                    out += g[(r, c)]
                elif r - y >= 0 and r - y < len(b) and c - x >= 0 and c - x < len(b[0]):
                    out += b[r - y][c - x]
                else:
                    out += '.'
            out += '|'
            print(out)
        print('     +-------+')
        print()

    while True:
        cmd = -1 if ps[cmd_index % len(ps)] == '<' else +1
        cmd_index += 1
        if can_move_to(x + cmd, y):
            x += cmd
        if can_move_to(x, y - 1):
            y -= 1
        else:
            put(x, y)
            if False and cmd_index % len(ps) == 0:
                print_cave()
            return (x, h - y)
        if False and cmd_index % len(ps) == 0:
            print_cave()


hs = []
cycle = None
begin = None
seen = {}

c = 0

def get_h(t, begin, cycle):
    h = ((t - begin) // cycle) * (hs[begin + cycle] - hs[begin])
    if (t - begin) % cycle + begin - 1 >= 0:
        h += hs[(t - begin) % cycle + begin - 1]
    return h

def depths(y):
    out = []
    for c in range(7):
        for r in reversed(range(-1, y)):
            if r == -1:
                out.append(None)
                break
            if (r, c) in g:
                out.append(y - r + 1)
                break

    return tuple(out)


while cycle == None or c < 10000:
    x = fall(blocks[c % len(blocks)])
    hs.append(h)
    if cycle == None:
        cc = cmd_index % len(ps)
        bc = (c + 1) % len(blocks)

        key = (cc, bc, x, depths(h))
        if key in seen:
            cycle = c - seen[key]
            begin = seen[key]
        else:
            seen[key] = c
    c += 1



# sanity check
for t in range(begin + 1, len(hs)):
    if get_h(t, begin, cycle) != hs[t - 1]:
        print("begin:", begin, "cycle:", cycle, "t:", t, get_h(t, begin, cycle), "!=", hs[t - 1])
        exit(1)

print(get_h(2022, begin, cycle))
print(get_h(1000000000000, begin, cycle))

