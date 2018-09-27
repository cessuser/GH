from otree.api import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):

        yield (pages.Demographics, {
            'q1': 22,
            'q2': 'Female',
            'q3': 'Yes',
            'q4': 'Mathematical',
            'q5': 'Graduate',
            'q6': '1'

        })
        yield (pages.Demographics2, {
            'q7': '1',
            'q8': '1',
            'q9': 'Agree',
            'q10': 'Agree',
            'q11': '2',
            'q12': '2',
            'q13': '2'

        })
        yield (pages.Demographics3, {
            'q14': 'Klee-Bazille',
            'q15': '2',
            'q16': '1',
            'q17': '2',
            'q18': '1',
            'q19': 'Try to maximize my number of tokens.',
            'other': ''
        })
        yield (pages.Demographics4, {
            'q20a': 'test',
            'q20b': 'test',
            'q20c': 'test',
            'q21': '0',
            'q22': 'Klee',
            'klee': '2'

        })