#!/usr/bin/python3
"""
 Module 6-square
 Defines class square with private size and position attribute,
 Contains public area and  my_print method
"""


class Square:
    """
    Defines Square Class

    Args:
      size (int): size of a side of square
      position (tuple): position of square on coordinate

    Functions:
      __init__(self)
      size(self)
      size(self, value)
      area(self)
      my_print(self)
      position(self)
      pisition(self, value)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initilizes instance

        Args:
          size (int): size of side of square, default 0
          position (tuple): postion of square on cooordinate, default 0, 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter

        Returns; size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
          value (int): set size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Return: postion, if positionis tuple of 2 value
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        calculate area of square

        Return: area
        """
        return (self.__size)**2

    def my_print(self):
        """
        print square with # character
        """
        for height in range(self.__size):
            for space in range(self.__position[0]):
                print("_", end="")
            for width in range(self.__size):
                print("#", end="")
            print("")
