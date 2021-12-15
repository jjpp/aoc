#!/usr/bin/python3

i = '1113222113'

def expand(s):
    o = ''

    count = 0

    for c in s:
        if count == 0:
            p = c
            count = 1
        else:
            if p == c:
                count += 1
            else:
                o += str(count) + p
                count = 1
                p = c
    if count > 0:
        o += str(count) + p

    return o

for z in range(0, 40):
    i = expand(i)

print(len(i))
    
for z in range(0, 10):
    i = expand(i)

print(len(i))

