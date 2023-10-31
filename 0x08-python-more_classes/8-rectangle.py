#!/usr/bin/python3

"""
Module 8-rectangle

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
        __str__(seilf)
        __repr__(self)
        __del__(self)
        bigger_or_equal(rect_1, rect_2)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return a string representation of the rectangle with # signs"""
        rec = ""

        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec += str(self.print_symbol)
            rec += "\n"
        return rec

    def __repr__(self):
        """Return a string representation of the rectangle class"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes the rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return a retcangle with bigger area, or rect_1 otherwise"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
