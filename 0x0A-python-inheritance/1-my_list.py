#!/usr/bin/python3
'''
Module 1-my_list
inherits and prints a sorted list
'''


class MyList(list):
    '''
    inherits a list
    Functions:
        print_sorted
    '''

    def print_sorted(self):
        ''' prints a sorted list '''
        print(sorted(self))
