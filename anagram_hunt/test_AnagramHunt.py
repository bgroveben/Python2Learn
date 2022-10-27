import unittest
from AnagramHunt import AnagramHunt

class TestAnagramHunt(unittest.TestCase):

    def setUp(self):
        self.word_length = AnagramHunt.valid_len('6')

    def test_set_word_length_and_valid_len(self):
        self.assertTrue(self.word_length)
        self.assertIsInstance(self.word_length, int)

if __name__ == '__main__':
    main()
