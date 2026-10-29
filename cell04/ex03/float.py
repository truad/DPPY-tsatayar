#!/usr/bin/env python3

number_text = input('Give me a number: ')

number_float = float(number_text)

if number_float.is_integer():
    print('This number is integer.')
else:
    print('This number is decimal.')
