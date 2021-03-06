from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class EarningTaskIntro(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaxTransferIntro2(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaxTransferIntro(Page):
    def is_displayed(self):
        return self.round_number == 1


class taskPage_ET(Page):
    form_model = models.Player
    form_fields = ['entry_field']
    timeout_seconds = 90


    def is_displayed(self):
        print("round: ", self.round_number)
        if self.round_number == 1:
            self.player.participant.vars['remaining_time'] = 90
        self.player.participant.vars['time_onLoad'] = time.time()
        return self.player.participant.vars['remaining_time'] > 0 and 1 <= self.round_number <= 30

    def get_timeout_seconds(self):
        print("remain time: ", self.participant.vars['remaining_time'])
        return self.player.participant.vars['remaining_time']

    def vars_for_template(self):
        if self.round_number == 1:
            self.participant.vars['ET1_incorrect'] = []
            self.participant.vars['ET1_correct'] = 0
        self.participant.vars['ET1_incorrect'].append(0)
        return{
            'round_num': self.round_number,
            'shown_num': Constants.shown_nums[self.round_number-1]
        }

    def entry_field_error_message(self, value):
        if value != len(str(Constants.shown_nums[self.round_number-1])):
            self.participant.vars['ET1_incorrect'][self.round_number-1] += 1
            return 'Please enter the right digit number '

    def before_next_page(self):
        spent = time.time() - self.player.participant.vars['time_onLoad']

        self.participant.vars['remaining_time'] = self.player.participant.vars['remaining_time'] - spent
        if self.player.entry_field == len(str(Constants.shown_nums[self.round_number-1])):
            self.participant.vars['ET1_correct'] += 1
        if self.timeout_happened:
            self.participant.vars['remaining_time'] = 0
        self.player.set_nt1_points()
        print("pid: ", self.player.id_in_group, "remaining time: ", self.player.participant.vars['remaining_time'])


page_sequence = [
    Introduction,
    EarningTaskIntro,
    TaxTransferIntro,
    TaxTransferIntro2,
    taskPage_ET
]
