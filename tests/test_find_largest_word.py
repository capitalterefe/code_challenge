import unittest
from pathlib import Path
from words.find_largest_word import LargestWord


class find_largest_word_test(unittest.TestCase):
    def setUp(self):
        self.find_largest_word = LargestWord()

    def test_largest_word(self):  # verify the first largest word should be returned
        valid_data = self.find_largest_word.get_largest_word(
            Path('valid_data.txt').read_text())
        self.assertEqual(valid_data, 'possible')

    # verify the first largest word is transposed
    def test_transpose_withValidData(self):
        valid_data = self.find_largest_word.transpose_largest_word(
            Path('valid_data.txt').read_text())
        self.assertEqual(valid_data, 'elbissop')

    # Verify if no data provided it should return None
    def test_isEmptyDataAccepted(self):
        self.assertIsNone(self.find_largest_word.get_largest_word(''))

    # Verify special characters get stripped out, retun None if only special characters and numbers provided
    def test_special_characters(self):
        self.assertIsNone(
            self.find_largest_word.get_largest_word('*#! *%@28}!'))

    # Verify exception will be thrown if None passed as a data
    def test_TypeErrorExceptions(self):
        with self.assertRaises(TypeError):
            self.find_largest_word.get_largest_word(None)


if __name__ == "__main__":
    unittest.main()
