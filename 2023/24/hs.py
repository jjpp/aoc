#!/usr/bin/python3

import sys

ls = [l.strip() for l in sys.stdin]

ps = []
vs = []
aa = []
bb = []

for l in ls:
    (p, v) = l.split(' @ ')
    ps.append([int(x) for x in p.split(', ')])
    vs.append([int(x) for x in v.split(', ')])

min_xy = 200000000000000
max_xy = 400000000000000

def solution_in(a, b, min_xy, max_xy):

    # min_xy <= x <= max_xy
    # min_xy <= y <= max_xy

    # aa = vay / vax
    # ab = vby / vbx
    # ba = pay - aa * pax = pay - (vay / vax) * pax
    # bb = pby - ab * pbx

    # y = aa * x + ba
    # y = ab * x + bb
    # aa * x + ab = ab * x + bb
    # x = (bb - ab) / (aa - ba)


    # (vay / vax) * x + (pay - pax*vay/vax) = (vby / vbx) * x + (pby - pbx*vby/vbx)
    # (vay / vax - vby / vbx) * x = (pby - pbx*vby/vbx - pay + pax*vay/vax) 

    # Hailstone A: 19, 13, 30 @ -2, 1, -2
    # Hailstone B: 18, 19, 22 @ -1, -1, -2
    # Hailstones' paths will cross inside the test area (at x=14.333, y=15.333).
    # aa = -1/2
    # ba = 1
    # ab = 13 - aa * 19 = 13 + 19/2 = 22.5
    # bb = 5
    # x = 


    print(a, b)
    print(ps[a], vs[a])
    print(ps[b], vs[b])

    if vs[a][0] == 0:
        print("vax == 0")
        exit(1)
        return False
    if vs[b][0] == 0:
        print("vbx == 0")
        exit(1)
        return False

    aa = vs[a][1] / vs[a][0]
    ab = vs[b][1] / vs[b][0]
    ba = ps[a][1] - aa * ps[a][0]
    bb = ps[b][1] - ab * ps[b][0]

    print("aa =", aa)
    print("ab =", ab)
    print("ba =", ba)
    print("bb =", bb)

    if aa == ab:
        # parallel
        if (ps[a][0] == ps[b][0]) and (ps[a][1] == ps[b][1]):
            print("FOUND: parallel but at the same point?")
            return True
        if vs[a][0] == vs[b][0]:
            return False
        # ya = aa * xa + ab
        # yb = ba * xb + bb
        # xa = pax + t*vax
        # xb = pbx + t*vbx
        # pax + t * vax = pbx + t * vbx
        # t (vax - vbx) = pbx - pax
        # t = (pbx - pax) / (vax - vbx)
        t_x = (ps[b][0] - ps[a][0]) / (vs[a][0] - vs[b][0])
        t_y = (ps[b][1] - ps[a][1]) / (vs[a][1] - vs[b][1])
        print("t_x =", t_x)
        print("t_y =", t_y)
        if (t_x >= 0) and abs(t_x - t_y) < 0.0000001:
            print("FOUND")

        return (t_x >= 0) and abs(t_x - t_y) < 0.0000001

    x = (bb - ba) / (aa - ab)
    print("x =", x)
    y = ab * x + bb
    if y != aa * x + ba:
        print("hm: ", ab * x + bb, aa * x + ba)
    #    exit(1)

    print("y =", y)

    if x < min_xy or x > max_xy or y < min_xy or y > max_xy:
        # outside the area
        print("outside the area")
        return False

    # x = pax + t * vax
    # t = (x - pax) / vax

    t_a = (x - ps[a][0]) / vs[a][0]
    t_b = (x - ps[b][0]) / vs[b][0]

    print("t_a =", t_a)
    print("t_b =", t_b)
    if t_a >= 0 and t_b >= 0:
        print("FOUND")
    return t_a >= 0 and t_b >= 0


count = 0

#min_xy = 7
#max_xy = 27

for a in range(0, len(ls) - 1):
    for b in range(a + 1, len(ls)):
        count += 1 if solution_in(a, b, min_xy, max_xy) else 0

print(count)


