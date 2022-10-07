import unittest
from AnagramHunt import AnagramHunt

class TestValidLen(unittest.TestCase):

    def test_set_word_length_and_valid_len(self):
        self.assertTrue(AnagramHunt.valid_len('6'))
        self.assertIsInstance(AnagramHunt.valid_len('6'), int)

    def test_gameplay(self):
        pass


if __name__ == '__main__':
    main()
