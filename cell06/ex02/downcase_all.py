#!/usr/bin/env python3

import sys

def downcase_it(s: str) -> str:
    return s.lower()


n = len(sys.argv)
args = sys.argv[1:n]

if len(args) < 1:
    print('none')
else:
    for arg in args:
        print(downcase_it(arg))