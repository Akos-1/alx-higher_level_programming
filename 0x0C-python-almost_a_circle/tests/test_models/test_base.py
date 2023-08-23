#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):

    def test_id_increment(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_assignment(self):
        obj_with_id = Base(id = 10)


        self.assertEqual(obj_with_id.id, 10)

if __name__ =='__main__':
    unittest.main()
