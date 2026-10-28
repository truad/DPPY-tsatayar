#!/usr/bin/env python3

def add2(val):
    return val + 2


original = [2, 8, 9, 48, 8, 22, -12, 2]
new = list(map(add2, original))

print('Original array: ', original)
print('New array: ', new)