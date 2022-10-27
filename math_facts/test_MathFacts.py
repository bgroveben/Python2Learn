import unittest
import time
from MathFacts import MathFacts


class TestMathFactsFunctions(unittest.TestCase):

    def setUp(self):
        self.valid_op = MathFacts.valid_op('+')
        self.valid_num = MathFacts.valid_num('100')

    def test_choose_op_and_valid_op(self):
        self.assertIsInstance(self.valid_op, bool)
        self.assertTrue(self.valid_op)

    def test_set_max_num_and_valid_num(self):
        self.assertIsInstance(MathFacts.valid_num('100'), int)
        self.assertTrue(MathFacts.valid_num('100'))
        self.assertIsInstance(MathFacts.valid_num('100'), int)

if __name__ == '__main__':
    main()
