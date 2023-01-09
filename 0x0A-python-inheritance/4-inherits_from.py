#!/usr/bin/python3
'''
Module 4-inherits_from
'''


def inherits_from(obj, a_class):
    ''' uses type and issubclass to checks wether an objects inherits '''

    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
