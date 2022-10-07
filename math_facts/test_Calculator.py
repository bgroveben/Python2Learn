import unittest
from Calculator import Calculator

class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        self.addition = Calculator(2,2,'+')
        self.subtraction = Calculator(10,9,'-')
        self.multiplication = Calculator(3,4,'*')
        self.division = Calculator(10,2,'/')

    def test_add(self):
        self.assertEqual(self.addition.result, 4)
    def test_subtract(self):
        self.assertEqual(self.subtraction.result, 1)
    def test_multiply(self):
        self.assertEqual(self.multiplication.result, 12)
    def test_divide(self):
        self.assertEqual(self.division.result, 5.0)


if __name__ == '__main__':
    unittest.main()
