import unittest
from lsn13 import Fraction


class FractionTestCase(unittest.TestCase):

    def setUp(self):
        self.x = Fraction(1, 2)
        self.y = Fraction(1, 4)

    def test_add(self):
        self.assertEqual(str(self.x + self.y), '3/4')

    def test_sub(self):
        self.assertEqual(str(self.x - self.y), '-1/4')

    def test_mul(self):
        self.assertEqual(str(self.x * self.y), '1/8')

    def test_truediv(self):
        self.assertEqual(str(self.x / self.y), '2/1')


unittest.main()
