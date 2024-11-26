# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # This should pass

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # This should pass

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)  # This should pass

    def test_divide(self):
        self.assertEqual(divide(10, 0), "Cannot divide by zero")  # This should pass

    def test_add_fail(self):
        self.assertEqual(add(2, 2), 4)  # This should pass

    def test_subtract_fail(self):
        self.assertEqual(subtract(5, 5), 0)  # This should pass

if __name__ == '__main__':
    unittest.main()
