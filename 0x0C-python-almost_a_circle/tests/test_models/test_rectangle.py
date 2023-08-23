#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_attributes(self):
        r = Rectangle(10, 20, 5, 7, 1)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_rectangle_setters(self):
        r = Rectangle(10, 20, 5, 7, 1)

        r.width = 30
        r.height = 40
        r.x = 15
        r.y = 25

        self.assertEqual(r.width, 30)
        self.assertEqual(r.heigth, 40)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 25)


if __name__ = '__main__':
    unittest.main()
