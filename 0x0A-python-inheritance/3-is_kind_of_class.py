#!/usr/bin/python3
'''
Module 3-is_kind_of_class
checks if a class is inherited or not
'''


def is_kind_of_class(obj, a_class):
    '''
    checks isinstance of a class
    '''

    if isinstance(obj, a_class):
        return True
    else:
        return False
