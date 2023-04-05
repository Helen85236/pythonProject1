import unittest

from src.divide import divide
class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(100, 5), 20)
        self.assertEqual(divide(6, 2), 3)

    def test_divide__division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)