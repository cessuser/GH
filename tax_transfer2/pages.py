from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random


class MyPage(Page):
    def vars_for_template(self):
        return{
            "group_by_id" : self.player.participant.vars['pt_group_id']
        }


class WaitOther(WaitPage):
    body_text = 'We are calculating your tokens.Please wait.'

    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.set_rank_income2()


class Results_ET(Page):
    def is_displayed(self):
        return self.round_number == 1


class Period2(Page):
    form_model = models.Player
    form_fields = ['dv']

    def dv_choices(self):
        choices = [[1, 'Scheme 1: 20% taxes and 100 tokens for each participant'],
                   [2, 'Scheme 2: 40% taxes and 200 tokens for each participant']]

        random.shuffle(choices)
        return choices

    def vars_for_template(self):
        if self.round_number == 1:
            self.player.participant.vars['competition_period2'] = []
            self.player.participant.vars['dv_period2'] = []
            self.player.participant.vars['rg_tokens_period2'] = []

        self.player.set_info(self.round_number)
        group_members_info = self.player.find_group_members_info(self.round_number)
        self.player.set_competition()
        competition_msg = ['won the competition and will keep their earnings',
                           'lost the competition and will lose 40 tokens from their earnings']

        return{
            'group': self.player.pt_group_id,
            'member1_group': group_members_info[0][0][0],
            'member1_tokens': group_members_info[0][0][1],
            'member2_group': group_members_info[0][1][0],
            'member2_tokens': group_members_info[0][1][1],
            'member3_group': group_members_info[0][2][0],
            'member3_tokens': group_members_info[0][2][1],
            '400token_group': group_members_info[1],
            'competition_msg': competition_msg[self.player.competition]
        }

    def before_next_page(self):
        self.player.participant.vars['dv_period2'].append(self.player.dv)


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 7

    def after_all_players_arrive(self):
        self.group.set_rg_tokens()
        self.group.set_rgab_tokens()


class MyPage(Page):
    def is_displayed(self):
        return self.round_number == 7

page_sequence = [
    WaitOther,
    Results_ET,
    Period2,
    ResultsWaitPage,
    MyPage
]
