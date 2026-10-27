#!/usr/bin/env python3

number_text = input()

if number_text.lstrip('+-').isnumeric():
    if int(number_text) == 0:
        print('This number is both positive and negative')
    elif int(number_text) < 0:
        print('This number is negative')
    else:
        print('This number is positive')