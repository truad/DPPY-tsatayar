#!/usr/bin/env python3

import sys

n = len(sys.argv)
args = sys.argv[1:n]


if (len(args) < 2):
    print('none')
else:
    for arg in reversed(args): print(arg)
