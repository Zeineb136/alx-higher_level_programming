#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """initialize the Rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of the rectangle
        Returns:
        the area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """calculates the perimeter of the rectangle
        Returns:
        the perimeter of the rectangle
        """
        return ((self.__height + self.__width) * 2)

    @property
    def height(self):
        """gets the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """gets the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __str__(self):
        """prints a rectangle"""
        str = ""
        if self.__height != 0 or self.__width != 0:
            str += '\n'.join('#' * self.__width for _ in range(self.__height))
        return (str)
        print()

    def __rep__(self):
        """return a string representation of the rectangle"""
        return("Rectangle({:}, {:})".format(str(self.__width), str(self.__height)))
