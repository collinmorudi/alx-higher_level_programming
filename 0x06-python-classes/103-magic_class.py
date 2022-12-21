"""Define MagicClass"""
import math


class MagicClass:
    """Initialize and define methods area and circumference of a circle"""
    def __init__(self, radius=0):
        """Init MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calcualte the circumference"""
        return 2 * math.pi * self.__radius
