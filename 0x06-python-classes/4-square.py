#!/usr/bin/python3
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

    @property
    def size(self):
        """ Method to returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
