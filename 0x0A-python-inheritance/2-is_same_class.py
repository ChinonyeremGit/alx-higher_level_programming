#!/usr/bin/python3
'''
Module 2-is_same_class
'''


def is_same_class(obj, a_class):
    '''
    checks isistance of an object
    '''

    if type(obj) == a_class:
        return True
    else:
        return False
