#!/usr/bin/python3

"""
Module 1-rectangle
Contains the class Rectangle
"""


class Rectangle:
    """
    Defines the rectangle class with private attributes width and height
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initializing the rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width of the """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets the width of the rectangle if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets the height of the rectangle if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
