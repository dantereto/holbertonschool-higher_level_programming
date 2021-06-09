#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestMaxInteger(unittest.TestCase):
    
    def test_cases(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
        b1 = Base(34)
        self.assertEqual(34, b1.id)
        b1 = Base(-1)
        self.assertEqual(-1, b1.id)
        b1 = Base('hola')
        self.assertEqual('hola', b1.id)
        b1 = Base({'id': 48, 'size': 12})
        self.assertEqual({'id': 48, 'size': 12}, b1.id)
        b1 = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b1.id)
        b1 = Base([1, 2, -3])
        self.assertEqual([1, 2, -3], b1.id)
if __name__ == '__main__':
    unittest.main()
