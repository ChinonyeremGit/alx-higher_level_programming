#!/usr/bin/python3
'''
Module 3-say_my_name

contains a function -say_my_name- to print a person's name
'''


def say_my_name(first_name, last_name=""):
    '''
    prints a person's name
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
