from pathlib import Path
import csv
from repositories.name_validation import NameValidator

class ScoreRepository:
    """
    Gamescore related database operations.
    """

    def __init__(self, file_path):
        """
        file_path (string): path to the file that holds dada
        """
        self.validator = NameValidator()
        self._file_path = file_path
        self._ensure_file_exists()


    def find_all(self):
        """
        Gets all names
        Return:
        """
        return self._read()

    def _read(self):
        """
        Makes sure that data file (.csv) exists
        Reads the file into tuple (name, score)
        Returns aforementioned list
        """
        scores = []
        self._ensure_file_exists()
        with open(self._file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    s_row = row
                    if ";" in row[0]:
                        s_row = row[0].split(";")
                    scores.append((s_row[0], float(s_row[1])))
        return scores

    def _ensure_file_exists(self):
        """
        """
        Path(self._file_path).touch()

    def new_score(self, name, score):
        """
        Handles adding new score+names to highscore
        """
        scores = self._read()
        validated_name = self.validator.string_validation(name)
        scores.append((validated_name, score))
        best_list = self.calc_ten_best(scores)
        with open(self._file_path, "w") as file:
            writer = csv.writer(file)
            for tuple in best_list:
                writer.writerow([tuple[0]]+[tuple[1]])

    def calc_ten_best(self, names_scores):
        """
        Orders list of tuples so that highest first
        Args:
        names_scores (list of tuples (name, score)):
        Returns:
        List of 10 highest score tuples
        """
        sorted_by_second_value = sorted(names_scores, key=lambda tup: tup[1], reverse=True)
        return sorted_by_second_value[:10]

    def find_all_string(self):
        """
        Returns:
        Gets all items from the _read function and converts them to a list of strings
        """
        tups = self._read()
        ret = list(map(lambda tup: tup[0]+" "+str(tup[1]), tups))
        return ret
