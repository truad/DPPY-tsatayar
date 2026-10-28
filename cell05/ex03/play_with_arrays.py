#!/usr/bin/env python3

original =  [2, 8, 9, 48, 8, 22, -12, 2]
target = []

for item in original:
  if (item > 5) and (not item+2 in target):
    target.append(item+2)

print('Original array: ', original)
print('New array: ', target)
