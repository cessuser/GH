from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = ''


class Constants(BaseConstants):
    name_in_url = 'earning_task3'
    players_per_group = None

    num_rounds = 30


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nt3_points = models.IntegerField()
    entry_field = models.IntegerField()
    time_out_happened = models.BooleanField()
    shown_num = models.IntegerField()

    def set_shown_num(self):
        if self.participant.vars['income2'] in [800, 600]:
            self.shown_num = random.randint(10**3, 10**random.randint(6, 14))
        else:
            self.shown_num = random.randint(10**3, 10**random.randint(6, 10))

    def set_nt3_points(self):
        self.nt3_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt1_points -= 10
        self.participant.vars['nt3_points'] = self.nt3_points


