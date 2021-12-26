from pathlib import Path
import csv
import os
from os.path import dirname, abspath
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
        dirr = Path(__file__).resolve().parents[2]
        dirr = str(dirr)+"\data"
        exists = os.path.exists(dirr)
        if not exists:
            os.makedirs(dirr)
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
                    if len(s_row[1]) > 0:
                        scores.append((s_row[0], float(s_row[1])))
                    else:
                        scores.append((s_row[0], s_row[1]))
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
        self._write(best_list)

    def calc_ten_best(self, names_scores):
        """
        Orders list of tuples so that highest first
        Args:
        names_scores (list of tuples (name, score)):
        Returns:
        List of 10 highest score tuples
        """
        names_scores = self._remove_empties(names_scores)
        sorted_by_second_value = sorted(names_scores, key=lambda tup: tup[1], reverse=True)
        return sorted_by_second_value[:10]

    def _remove_empties(self, names_score):
        ret = []
        for tup in names_score:
            if not isinstance((tup[1]), str):
                ret.append(tup)
        return ret

    def find_all_string(self):
        """
        Returns:
        Gets all items from the _read function and converts them to a list of strings
        """
        tups = self._read()
        ret = list(map(lambda tup: tup[0]+" "+str(tup[1]), tups))
        return ret

    def delete_all(self):
        """
        writes empty list
        """
        self._write_only([("", "")])

    def _write_only(self, name_scores):
        self._ensure_file_exists()
        with open(self._file_path, "w") as file:
            for names in name_scores:
                row = f'{names[0]};{names[1]}'
                file.write(row+'\n')


    def _write(self, list_of_tuples):
        self._ensure_file_exists()
        with open(self._file_path, "w") as file:
            writer = csv.writer(file)
            for tup in list_of_tuples:
                writer.writerow([tup[0]]+[tup[1]])
