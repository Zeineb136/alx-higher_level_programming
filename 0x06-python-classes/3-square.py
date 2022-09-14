#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """size is a Private instance attribute
    Attributes:
        size     size of the square
    """
    def __init__(self, size=0):
        """initialize  the Square
        Args:
        size    size of the square
        Returns:
            None
        """
    self.__size = size
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    def area(self):
        """calculates the area of the square
        Returns:
        the area of the square
        """
        return self.__size**2
