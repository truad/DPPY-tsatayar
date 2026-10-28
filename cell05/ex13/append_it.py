#!/usr/bin/env python3

import sys

n = len(sys.argv)
args = sys.argv[1:n]

for arg in args:
        # print(a)
    if arg.endswith("ism"):
        print(arg)
    else:
        print(f'{arg}ism')