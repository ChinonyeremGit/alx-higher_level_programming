#!/usr/bin/python3
'''
Module 5-base_geometry
contains class base geometry and rectangle
'''


class BaseGeometry:
    '''
    raises an exception
    Functions:
        area(self)
        integer_validator
    '''

    def area(self):
        ''' funtion to raise an exception for now '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        validates an integer
        Args:
            name (str): a string describing the type of value
            value (int): value to validate
        '''

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    '''
    inherits from a class
    Args:
        width: width of rectangle
        height: height of reactangle
    Functions:
        __init__(self, width, height)
    '''

    def __init__(self, width, height):
        ''' initializer '''

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
