#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestMaxInteger(unittest.TestCase):
    def test_cases(self):
        s1 = Square(5)
        self.assertEqual(5, s1.width)
        self.assertEqual(5, s1.height)
        s3 = Square(3, 1, 3, 12)
        self.assertEqual(12, s3.id)
        s3 = Square(3, 1)
        self.assertEqual(3 * 3, s3.area())
        s3 = Square(3, 1, 12, 4)
        self.assertEqual(3 * 3, s3.area())
        s1.update(43)
        self.assertEqual(43, s1.id)
        s1.update(43, 98)
        self.assertEqual(98, s1.size)
        s1.update(43, 98, 3)
        self.assertEqual(3, s1.x)
        s1.update(43, 98, 3, 21)
        self.assertEqual(21, s1.y)
        s1.update(size=13, id=22, y=1, x=12)
        self.assertEqual(22, s1.id)
        self.assertEqual(13, s1.size)
        self.assertEqual(12, s1.x)
        self.assertEqual(1, s1.y)
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 3, 'x': 2, 'size': 10, 'y': 1})
    def error_cases(self):
        with self.assertRaises(TypeError):
             r = Square('10')
        with self.assertRaises(TypeError):
            r = Square('gol')
        with self.assertRaises(TypeError):
            r = Square([2, 3])
        with self.assertRaises(TypeError):
            r = Square(2, '3')
        with self.assertRaises(TypeError):
            r = Square(2, 'hola')
        with self.assertRaises(TypeError):
            r = Square('2', 3)
        with self.assertRaises(TypeError):
            r = Square('adios', 3)
        with self.assertRaises(TypeError):
             r = Square(True, 3)
        with self.assertRaises(TypeError):
            r = Square(3, False)
        with self.assertRaises(ValueError):
            r = Square(-2, 3)
        with self.assertRaises(ValueError):
            r = Square(2, -3)
        with self.assertRaises(ValueError):
            r = Square(2, 3.9)
        with self.assertRaises(ValueError):
            r = Square(2.0, 3)
        with self.assertRaises(ValueError):
            r = Square(-3)
        with self.assertRaises(ValueError):
            r = Square(3.9)

if __name__ == '__main__':
    unittest.main()
