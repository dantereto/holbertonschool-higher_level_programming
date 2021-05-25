#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([3, 6, 4 , 5]), 6)
        self.assertEqual(max_integer([20, 20, 20, 20]), 20)
        self.assertEqual(max_integer([20, 20, 20, 20]), 20)
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-55, -68, -1, -32]), -1)
        self.assertEqual(max_integer([1.1, 2.2, 78.2, 5,5]), 78.2)
        self.assertEqual(max_integer([-1.1, -2.2, -78.2, -5.5]), -1.1)
        self.assertEqual(max_integer("1, 4, 5, 6, 10"), "6")
        self.assertEqual(max_integer('123456789'), '9')
        self.assertEqual(max_integer([[1, 2, -3, 4], [10, 30, 50, 70]]), [10, 30, 50, 70])
        self.assertEqual(max_integer("x, a, b, c, d"), "x")
        self.assertEqual(max_integer("1, z, 5, 4, i"), "z")
        self.assertEqual(max_integer([0]), 0)
        
    def test_error(self):
        with self.assertRaises(TypeError):
            max_integer(4, 'hola')
        with self.assertRaises(TypeError):
            max_integer(4)
        with self.assertRaises(TypeError):
            max_integer({4, 7})
        with self.assertRaises(KeyError):
            max_integer({'val': 3, 'vol': 7})
        with self.assertRaises(TypeError):
            max_integer([3, 6, 4, None, 5])
        with self.assertRaises(TypeError):
            max_integer(None)
if __name__ == '__main__':
    unittest.main()
