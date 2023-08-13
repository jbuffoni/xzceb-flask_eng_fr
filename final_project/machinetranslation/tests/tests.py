import unittest
from translator import english_to_french, french_to_english

class TestTranslatorFunctions(unittest.TestCase):

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english_hello(self):
        self.assertEqual(french_to_english("Hello"), "Hello")

    def test_english_to_french_bonjour(self):
        self.assertEqual(english_to_french("Bonjour"), "Bonjour")

    def test_french_to_english_bonjour(self):
        self.assertIn(french_to_english("Bonjour"), ["Hello", "Hi"])

if __name__ == "__main__":
    unittest.main()