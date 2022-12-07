#!/usr/bin/python3

import sys
from collections import Counter

ls = [l.strip() for l in sys.stdin]

def rot(s, n):
    return "".join([chr(ord('a') + ((ord(c) - ord('a') + n) % 26)) for c in s])

rooms = []
for r in ls:
    chars = r.split('-')
    (sector, checksum) = chars.pop().split('[')
    checksum = checksum[:-1]
    sector = int(sector)
    counts = Counter("".join(chars))
    rs = "".join([x[0] for x in sorted(counts.items(), key = lambda x : (-x[1], x[0]))][0:5])
    if rs == checksum:
        decrypted = [rot(w, sector) for w in chars]
        rooms.append([chars, sector, checksum, " ".join(decrypted)])




print(sum([r[1] for r in rooms]))
print(min([r[1] for r in rooms if r[3] == 'northpole object storage']))
