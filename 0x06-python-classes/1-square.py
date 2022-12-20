#!/usr/bin/python3
"""
File: 1-square
Defines the class Square with private attribute size
"""


class Square:
    """
    class Square definition
    Args:
        size : size of the sides
    """
    def __init__(self, size):
        """
        Init square
        Attributes:
            size: size of the sides
        """
        self.__size = size
