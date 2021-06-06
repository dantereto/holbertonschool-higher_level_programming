#!/usr/bin/python3
"""start the functions"""


from models.base import Base


class Rectangle(Base):
    """start"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__y):
            print('')
        for j in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        return ("[{}] ({}) {:d}/{:d} - {:d}/{:d}".format
                ('Rectangle', self.id, self.__x, self.__y,
                 self.__width, self.__height))

    def update(self, *args, **kwargs):
        if args:
            if len(args) == 0:
                self.id = args[0]
            if len(args) == 1:
                self.__width = args[1]
            if len(args) == 2:
                self.__height = args[2]
            if len(args) == 3:
                self.__x = args[3]
            if len(args) == 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dict_r = {'id': self.id, 'width': self.width,
                  'height': self.height, 'x': self.x, 'y': self.y}
        return (dict_r)
