#!/usr/bin/python3

import sys
import re
from queue import PriorityQueue

ls = [l.strip() for l in sys.stdin]

def nums(l):
    return list(map(int, re.findall("-?\\d+", l)))

g = {}

for l in ls:
    d = l.split(' ')
    frm = d.pop(0)
    frm = frm[0:-1]

    g[frm] = set(d)

def bfs(frm):
    w = {}
    q = PriorityQueue()
    q.put((0, frm, ''))

    while not q.empty():
        (d, pos, path) = q.get()
        if pos not in w:
            w[pos] = set()

#        print(d, pos, path)

        if path not in w[pos]:
            w[pos].add(path)
            if pos in g:
                for to in g[pos]:
                    q.put((d + 1, to, path + ";" + to))
    return w

def bfs2(frm):
    w = {}
    in_queue = set()
    q = PriorityQueue()
    q.put((0, frm, ''))

    w[''] = {}
    w['']['total'] = 1

    while not q.empty():
        (d, pos, f) = q.get()
        if pos not in w:
            w[pos] = {}

        if (d, pos, f) in in_queue:
            in_queue.remove((d, pos, f))

        if f not in w[pos] or w[pos][f] < w[f]['total']:
            oldf = w[pos].get(f, 0)
            total = w[pos].get('total', 0)
            w[pos][f] = w[f]['total']
            w[pos]['total'] = total + w[f]['total'] - oldf

            if pos in g:
                for to in g[pos]:
                    nd = d + 1
                    if (nd, to, pos) not in in_queue:
                        q.put((nd, to, pos))
    return w


w = bfs('you')
if 'out' in w:
    print(len(w['out']))

full = bfs2('svr')
frm_fft = bfs2('fft')
frm_dac = bfs2('dac')

print(full['fft']['total'] * frm_fft['dac']['total'] * frm_dac['out']['total'])

