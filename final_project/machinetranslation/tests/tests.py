import unittest
from translator import english_to_french, french_to_english

class FrenchToEnglishTranslatorTest(unittest.TestCase):
    def test_doesnt_process_null(self):
        french = None
        
        output = french_to_english(french)

        self.assertIsNone(output)

    
    def test_translates_properly(self):
        french = "Bonjour"
        
        english = french_to_english(french)

        self.assertEqual(english, "Hello")


class EnglishToFrenchTranslatorTest(unittest.TestCase):
    def test_doesnt_process_null(self):
        english = None
        
        output = english_to_french(english)

        self.assertIsNone(output)

    def test_translates_properly(self):
        english = "Hello"
        
        french = english_to_french(english)

        self.assertEqual(french, "Bonjour")

if __name__ == '__main__':
    unittest.main()

