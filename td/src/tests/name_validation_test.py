import unittest
import random
from repositories.name_validation import NameValidator

class TestNameValidator(unittest.TestCase):
    """
    ()_(o.o)_() snib snab
    """

    def setUp(self):
        self.validator = NameValidator()

    def test_string_validation(self):
        """
        a is added so that string_validation doesn't add a random name from the random
            name generator
        """
        char_list = ["%", "2", "&", ".", "_", "", "f9f", "%", "(", "/", "(#"]
        test_str = ""
        for i in range(1,10):
            index = random.randint(0, len(char_list)-1)
            test_str += char_list[index]
        test_str += "a"
        self.assertEqual(test_str.isalpha(), False)
        rectified = self.validator.string_validation(test_str)
        self.assertEqual(rectified.isalpha(), True)

    def test_name_randomizer(self):
        """
        if name lists are removed from config file, this will fail
        """
        for i in range(0,10):
            name = self.validator.name_randomizer()
            self.assertGreater(len(name), 0)
