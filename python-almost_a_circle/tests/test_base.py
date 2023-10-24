import unittest
from models.base import Base

class TestBase(unittest.TestBase):
    def test_1(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_2(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_3(self):
        b = Base(100000)
        self.assertEqual(b.id, 100000)

    def test_4(self):
        b = Base()

    if __name__ == '__main__':
        unittest.main()