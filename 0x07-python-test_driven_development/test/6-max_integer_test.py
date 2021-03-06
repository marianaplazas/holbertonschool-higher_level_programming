#!/usr/bin/python3
"""
this is a unitte test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxMatrix(unittest.TestCase):
    def max_basic(self):
        self.assertMax(max_integer([200, 3, 2, 2,4]), 200)

    def error(self):
        self.assertEmpty(max_integer())

    def test_not_int(self):
        with self.assertRaise(TypeError):
            max_integer([3, 5, 7, "String"])

if __name__ == '__main__':
    unittest.main()
