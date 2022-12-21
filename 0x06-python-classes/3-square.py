#!/usr/bin/python3
"""
File 3-square
Defines class Square with private attribute size and public attribute area
"""


class Square:
    """ A class that defines a square by its side size
    """
    def __init__(self, size=0):
        """ Method to init the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)
