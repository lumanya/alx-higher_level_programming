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
    size(self)
    size(self, value)
    update(self, *args, **kwargs)
    to_dictionary(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializing instance of the class and inherting"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter pf size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ return dictionary representaion of an instance"""
        dict_rep = {'id': self.id, 'size': self.size, 'x': self.x,
                    'y': self.y}
        return dict_rep

    def update(self, *args, **kwargs):
        """assign attributes"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """ Print [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.height)
