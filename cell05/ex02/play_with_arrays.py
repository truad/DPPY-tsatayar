#!/usr/bin/env python3

original =  [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for item in original:
  if item > 5:
    new.append(item+2)

print('Original array: ', original)
print('New array: ', new)
