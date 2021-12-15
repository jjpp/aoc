#!/usr/bin/python3

import sys

sum = 0
ribbon = 0

for line in sys.stdin:
    [a, b, c] = line.split('x')
    a = int(a)
    b = int(b)
    c = int(c)
    sum += (2*a*b) + (2*a*c) + (2*b*c)
    s1 = min(a, min(b, c))
    s2 = a + b + c - max(a, max(b, c)) - s1
    sum += (s1*s2)
    ribbon += (s1+s1+s2+s2)
    ribbon += a*b*c

print(sum)
print(ribbon)

