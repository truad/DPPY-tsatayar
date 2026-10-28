#!/usr/bin/env python3

import sys

args = sys.argv

i = 1

while i < len(sys.argv):
    arg = sys.argv[i]
    if arg.isalpha(): print(arg); break;
    i += 1