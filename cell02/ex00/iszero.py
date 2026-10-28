#!/usr/bin/env python3

number_text = input()
if number_text.isnumeric():
    if int(number_text) == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
