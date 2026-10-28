#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
  print('none')
else:
  i = 0
  while(i <= 10):
    table_row = ''
    j = 0

    while(j <= 10):
      table_row = table_row + f' {i*j}'
      j += 1

    print(f'Table de {i}:{table_row}')
    i += 1