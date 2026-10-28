#!/usr/bin/env python3

import sys

def shrink(s:str) -> str:
    return(s[0:8])

def enlarge(s:str) -> str:
    return s + 'z'*(8-len(s))

n = len(sys.argv)
args = sys.argv[1:n]

if len(args) < 1:
    print('none')
else:
    for arg in args:
        if len(arg) > 8 : print(shrink(arg))
        else : print(enlarge(arg))

