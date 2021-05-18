#!/usr/bin/python3
class Square:
     @property
     def size(self):
         return(self.__size)
     @size.setter
     def size(self, value):
          if type(value) is not int:
               raise TypeError('size must be an integer')
          if value < 0:
               raise ValueError('size must be >= 0')
          self.__size = value
     def area(self):
          return(self.__size ** 2)
def __eq__(self, other):
     return self.size == self.other
def __ne__(self, other):
     return self.size != self.other
def __gr__(self, other):
     return self.size > self.other
def __ge__(self, other):
     return self.size >= self.other
def __lt__(self, other):
     return self.size < self.other
def __le__(self, other):
     return self.size <= self.other
