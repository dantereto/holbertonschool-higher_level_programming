#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestMaxInteger(unittest.TestCase):
    def test_cases(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(10, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(10, r1.width)
        r3 = Rectangle(10, 2, 4, 5, 83)
        self.assertEqual(83, r3.id)
        r1 = Rectangle(3, 2)
        self.assertEqual(3 * 2, r1.area())
        r3 = Rectangle(2, 5, 0, 0, 12)
        self.assertEqual(2 * 5, r3.area())
        r1 = Rectangle(4, 6, 5, 2, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 5/2 - 4/6')
        r1.update(43)
        self.assertEqual(43, r1.id)
        r1.update(43, 1)
        self.assertEqual(1, r1.width)
        r1.update(43, 1, 144)
        self.assertEqual(144, r1.height)
        r1.update(43, 1, 144, 12)
        self.assertEqual(12, r1.x)
        r1.update(43, 1, 144, 12, 80)
        self.assertEqual(80, r1.y)
        r1.update(y=20, width=200, x=54, id=1, height=2)
        self.assertEqual(1, r1.id)
        self.assertEqual(200, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(54, r1.x)
        self.assertEqual(20, r1.y)
        
    def error_cases(self):
        with self.assertRaises(TypeError):
            r = Rectangle('10', 2)
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 'hola')
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -3, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, '2')
        with self.assertRaises(TypeError):
            r = Rectangle('adios', 2)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)
        

if __name__ == '__main__':
    unittest.main()
