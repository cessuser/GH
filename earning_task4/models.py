from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = ''


class Constants(BaseConstants):
    name_in_url = 'earning_task4'
    players_per_group = None

    num_rounds = 30

    num_len1 = [random.randint(10**3, 10**random.randint(6, 12)) for x in range(0,30)]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nt4_points = models.IntegerField()
    entry_field = models.IntegerField()
    time_out_happened = models.BooleanField()

    def set_nt4_points(self):
        self.nt4_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt4_points -= 10
        self.participant.vars['nt4_points'] = self.nt4_points


