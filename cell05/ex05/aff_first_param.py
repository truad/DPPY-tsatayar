#!/usr/bin/env python3

import sys

args = sys.argv

i = 1

while i < len(args):
    arg = args[i]
    if arg.isalpha(): print(arg); break;
    i += 1