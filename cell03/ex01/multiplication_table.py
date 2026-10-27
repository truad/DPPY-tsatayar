#!/usr/bin/env python3

number_text = input('Enter number\n')
number = int(number_text)

i = 0 
while i <= 9:
    print(f'{i} x {number} = {i*number}')
    i += 1
