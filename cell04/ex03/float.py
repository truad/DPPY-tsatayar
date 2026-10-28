#!/usr/bin/env python3

number_text = input('Give me a number: ')

number_float = float(number_text)
number_int = int(number_float)

if number_int == number_float:
    print('This number is integer.')
else:
    print('This number is decimal.')
