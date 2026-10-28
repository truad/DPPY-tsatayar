#!/usr/bin/env python3

stop_phrase = 'STOP'

user_input = input('What you gotta say? : ').strip()
while (user_input != stop_phrase):
  user_input = input('I got that! Anything else? : ').strip()