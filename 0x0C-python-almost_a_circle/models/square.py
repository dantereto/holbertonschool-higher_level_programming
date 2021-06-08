#!/usr/bin/python3
"""start the functions"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """funcion principal prueba"""

    def __init__(self, size, x=0, y=0, id=None):
        """funcion principal prueba"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """funcion principal prueba"""
        return "[{}] ({}) {:d}/{:d} - {:d}"\
            .format('Square', self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """funcion principal prueba"""
        return(self.height)
        return(self.width)

    @size.setter
    def size(self, value):
        """funcion principal prueba"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """funcion principal prueba"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """funcion principal prueba"""
        dict_s = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return (dict_s)
