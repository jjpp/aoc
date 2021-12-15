#!/usr/bin/python3

import hashlib

i = 'iwrupvqb'

n = 1

while not hashlib.md5((i + str(n)).encode()).hexdigest().startswith('000000'):
    n += 1

print(n)


