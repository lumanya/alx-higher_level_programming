#!/usr/bin/python3
"""
 square is the module that contains square class that inherit rectangel class
 and overloading __str__
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherit Rectangel class

    method:
     __str__(self)
    __init__(self, size, x=0, y=0, id=None
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializing instance of the class and inherting"""
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """ Print [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                self.id,self.x, self.y,
                                                self.height)
