import random
import re
from config import random_names_1, random_names_2

class NameValidator:
    """
    Used in score_repository to check that player passes only alphabetic
    characters as name.
    """
    def __init__(self):
        pass

    def string_validation(self, name_str):
        """
        Checks and cuts off non-alphabetic characters
        If result is empty, will give a name
        Args:
        name_str (string):
        """
        if len(name_str) == 0:
            return self.name_randomizer()
        if name_str.isalpha():
            return name_str
        rectified_name = re.sub('[^A-Za-z]+', '', name_str)
        if len(rectified_name) == 0:
            return self.name_randomizer()
        return rectified_name

    def name_randomizer(self):
        """
        If player has not provided a name lets random one.
        """
        name1 = random.choice(random_names_1)
        name2 = random.choice(random_names_2)
        return name1+"-"+name2
