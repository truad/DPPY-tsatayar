#!/usr/bin/env python3

import sys

n = len(sys.argv)
args = sys.argv[1:n]

output = ''

if len(args) != 1:
    print('none')
else:
    str = args[0]

    for char in str: 
        if char == 'z': output += 'z'
    if len(output) > 0:
        print(output)
    else:
        print('none')