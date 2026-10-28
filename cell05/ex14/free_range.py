#!/usr/bin/env python3

import sys

n = len(sys.argv)
args = sys.argv[1:n]

if len(args) != 2:
    print('none')
else:
    start = int(args[0])
    stop = int(args[1])
    range_array = list(range(start, stop+1, 1))
    print(range_array)