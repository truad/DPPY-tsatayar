#!/usr/bin/env python3

first_number = input('Enter the first number:\n')
second_number = input('Enter the second number:\n')
result = int(first_number) * int(second_number)

print(f'{first_number} x {second_number} = {result}')

if result == 0:
    print('The result is positive and negative')
elif result <0:
    print('The result is negative')
else:
    print('The result is positive')
