#!/usr/bin/python3

import sys
from collections import Counter

ls = [l.strip() for l in sys.stdin]
out = ""
out2 = ""

for i in range(0, len(ls[0])):
    c = Counter([l[i] for l in ls])
    out += c.most_common(1)[0][0]
    out2 += c.most_common()[-1][0]

print(out)
print(out2)
