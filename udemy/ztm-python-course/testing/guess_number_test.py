# Exercise Testing

import unittest
import guess_number


class TestGuessNumber(unittest.TestCase):
    def test_none_input(self):
        result = guess_number.getInput(None, 5)
        self.assertIsInstance(result, TypeError)

    def test_empty_string_input(self):
        result = guess_number.getInput('', 5)
        self.assertIsInstance(result, TypeError)

    def test_correct_input(self):
        result = guess_number.getInput(5, 5)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
