import unittest
from translator import english_to_french, french_to_english

class FrenchToEnglishTranslatorTest(unittest.TestCase):
    def test_doesnt_process_null(self):
        french = None
        
        output = french_to_english(french)

        self.assertIsNone(output)

    
    def test_translates_to_english(self):
        french = "Bonjour"
        
        english = french_to_english(french)

        self.assertEqual(english, "Hello")

    def test_changes_translated_text(self):
        french = "Bonjour"
        
        english = french_to_english(french)

        self.assertNotEqual(english, "Bonjour")


class EnglishToFrenchTranslatorTest(unittest.TestCase):
    def test_doesnt_process_null(self):
        english = None
        
        output = english_to_french(english)

        self.assertIsNone(output)

    def test_translates_properly(self):
        english = "Hello"
        
        french = english_to_french(english)

        self.assertEqual(french, "Bonjour")
    
    def test_changes_translated_text(self):
        english = "Hello"
        
        french = english_to_french(english)

        self.assertNotEqual(french, "Hello")

if __name__ == '__main__':
    unittest.main()

