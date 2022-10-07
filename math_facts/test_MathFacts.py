import unittest
import time
from MathFacts import MathFacts

class TestMathFactsFunctions(unittest.TestCase):
# Try using mocks?
# https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
    def test_choose_op(self):
        self._valid_op = MathFacts.valid_op('+') # return True if valid
        self.assertIsInstance(self._valid_op, bool)
        self.assertTrue(self._valid_op)

    def test_set_max_num_and_valid_num(self):
        self.assertIsInstance(MathFacts.valid_num('100'), int)
        self.assertTrue(MathFacts.valid_num('100'))
        self.assertIsInstance(MathFacts.valid_num('100'), int)

    def test_do_math(self):
        # Needs mocks
        pass

    def test_check_answer(self):
        # Needs mocks
        pass

    def test_validate_input_and_is_number(self):
        self.assertIsInstance(MathFacts.is_number('6'), int)
        self.assertTrue(MathFacts.is_number('6'))

    def test_run_game(self):
        pass


if __name__ == '__main__':
    main()
