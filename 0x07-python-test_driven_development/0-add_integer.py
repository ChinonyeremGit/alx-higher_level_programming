#!/usr/bin/python3
'''
Module 0-add_integer

Function to add two integers
'''

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
