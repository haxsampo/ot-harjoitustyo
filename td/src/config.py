import os
from dotenv import load_dotenv
"""
Contains database filename & path info
and random names lists
"""
dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

SCORES_FILENAME = os.getenv('SCORES_FILENAME') or "scores.csv"
SCORES_FILE = os.path.join(dirname, '..', 'data', SCORES_FILENAME)

random_names_1 = ['jonne',
                  'purjo',
                  'veeti',
                  'kuuno',
                  'pentti',
                  'make',
                  'laura',
                  'justiina']

random_names_2 = ['korianderi',
                  'taavetti',
                  'viljami',
                  'olavi',
                  'orvokki',
                  'kalevi',
                  'aukusti',
                  'pullervo',
                  'pontus',
                  'kamiina',
                  'justiina']
