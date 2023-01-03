#!/usr/bin/python3

"""
Module 1-rectangle
Contains the class Rectangle with private width and height
and public area and perimeter and it's string representation
and the delete method, and it has public attribute to keep
track of the number of instances.
"""


class Rectangle:
    """
    Defines the rectangle class with private attributes width and height
    Args:
        width (int): width
        height (int): height
    Attributes:
        number_of_instances (int)
        print_symbol (any type)
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        perimeter(self)
        area(self)
        __str__(self)
        __repr__(self)
        __del__(self)
        bigger_or_equal(rect_1, rect_2)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializing the rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """ Return width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        tmp = "\n".join([str(self.print_symbol) * self.__width
                        for rows in range(self.__height)])
        return tmp

    def __repr__(self):
        """ String representation to recreate new instance """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Deletes an instance of the class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
