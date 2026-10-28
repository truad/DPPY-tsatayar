#!/usr/bin/env python3

first_number_text = input('Give me the first number: ')
second_number_text = input('Give me the second number: ')

first_number = int(first_number_text)
second_number = int(second_number_text)

print('Thank you!')
print(f'{first_number} + {second_number} = {first_number + second_number}')
print(f'{first_number} - {second_number} = {first_number - second_number}')
print(f'{first_number} / {second_number} = {int(first_number / second_number)}')
print(f'{first_number} * {second_number} = {first_number * second_number}')
