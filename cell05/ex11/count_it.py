#!/usr/bin/env python3

import sys

n = len(sys.argv)
args = sys.argv[1:n]

if len(args) < 1:
    print('none')
else:
    print(f'parameters: {len(args)}')
    for param in args:
        print(f'{param}: ')
