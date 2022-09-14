#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """size is a Private instance attribute
    Attributes:
        __size: size of the square
    """
    def __init__(self, size=0):
        """initialize  the Square
        Args:
        size    size of the square
        Returns:
            None
        """
        self.__size = size

    def area(self):
        """calculates the area of the square
        Returns:
        the area of the square
        """
        return (self.__size)**2

    @property
    def size(self):
        """gets the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square"""
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
