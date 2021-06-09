#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestMaxInteger(unittest.TestCase):
    
    def test_cases(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
if __name__ == '__main__':
    unittest.main()
