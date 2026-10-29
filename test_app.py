import unittest
from app import add_numbers, get_greeting


class TestApp(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_get_greeting(self):
        self.assertEqual(get_greeting("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
