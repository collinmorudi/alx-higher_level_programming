#!/usr/bin/python3

"""
Module 3-rectangle

Rectangle class with pivate attributes width and height
"""


class Rectangle:
    """
    Creates a rectangle class with private instance attributes width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
    """

    def __init__(self, width=0, height=0):
        """Initialise Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width if value >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height if value is >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return a string representation of the rectangle with # signs"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join(["#" * self.__width for i in range(self.__height)])
        return rec
