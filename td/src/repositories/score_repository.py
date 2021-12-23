from pathlib import Path
import csv

class ScoreRepository:
    """
    Pisteisiin liittyvistä tietokantaoperaatiosta vastaava luokka.
    """

    def __init__(self, file_path):
        """
        file_path (string): polku tiedostoon, johon tehtävät tallennetaan
        """
        self._file_path = file_path
        self._ensure_file_exists()


    def find_all(self):
        """
        Hakee kaikki pisteet
        Return:

        """
        return self._read()

    def _read(self):
        scores = []
        self._ensure_file_exists()
        with open(self._file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append(row)


    def _ensure_file_exists(self):
        Path(self._file_path).touch()
