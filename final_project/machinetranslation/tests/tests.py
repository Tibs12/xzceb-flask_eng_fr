import unittest

from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_e2f_1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_e2f_2(self):
        self.assertNotEqual(english_to_french("chicken"), "truie")

    def test_f2e_1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_f2e_2(self):
        self.assertNotEqual(french_to_english("poulette"), "pig")

if __name__ == "__main__":
    unittest.main()