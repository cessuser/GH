from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np

author = 'Danlin Chen'

doc = """
tax and transfer period 3
"""


class Constants(BaseConstants):
    name_in_url = 'tax_transfer3'
    players_per_group = None
    num_rounds = 7


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_income3_by_rank(self, quartiles_lst, rank):
        if 0 <= rank < quartiles_lst[0]:
            return 800
        if quartiles_lst[0] <= rank < quartiles_lst[1]:
            return 600
        if quartiles_lst[1] <= rank < quartiles_lst[2]:
            return 400
        else:
            return 200

    def set_rank_income3(self):
        group1 = [[p.id,p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['pt_group_id'] == 1]
        group2 = [[p.id, p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['pt_group_id'] == 2]
        group3 = [[p.id, p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['pt_group_id'] == 3]

        group1 = sorted(group1, key=lambda x: x[1], reverse=True)
        group2 = sorted(group2, key=lambda x: x[1], reverse=True)
        group3 = sorted(group3, key=lambda x: x[1], reverse=True)

        group1 = [sort_p[0] for sort_p in group1]
        group2 = [sort_p[0] for sort_p in group2]
        group3 = [sort_p[0] for sort_p in group3]

        quartiles_group1 = [(len(group1) + 1) // 4, (len(group1)+1) // 2, (len(group1)+1)*3 // 4]
        quartiles_group2 = [(len(group2) + 1) // 4, (len(group2) + 1) // 2, (len(group2) + 1) * 3 // 4]
        quartiles_group3 = [(len(group3) + 1) // 4, (len(group3) + 1) // 2, (len(group3) + 1) * 3 // 4]

        for p in self.get_players():
            if p.id in group1:
                p.nt3_rank = group1.index(p.id) + 1
                p.participant.vars['nt3_rank'] = p.nt3_rank
                if p.participant.vars['n_group'] <= 3:
                    p.income3 = 800 - 200 * (p.nt3_rank-1)
                else:
                    p.income3 = self.set_income3_by_rank(quartiles_group1, p.nt3_rank-1)
                p.participant.vars['income3'] = p.income3
                p.participant.vars['income3'] = p.income3
            if p.id in group2:
                p.nt3_rank = group2.index(p.id) + 1
                p.participant.vars['nt3_rank'] = p.nt3_rank
                if p.participant.vars['n_group'] <= 3:
                    p.income3 = 800 - 200 * (p.nt3_rank-1)
                else:
                    p.income3 = self.set_income3_by_rank(quartiles_group2, p.nt3_rank-1)
                p.participant.vars['income3'] = p.income3
                p.participant.vars['income3'] = p.income3
            if p.id in group3:
                p.nt3_rank = group3.index(p.id) + 1
                p.participant.vars['nt3_rank'] = p.nt3_rank
                if p.participant.vars['n_group'] <= 3:
                    p.income3 = 800 - 200 * (p.nt3_rank-1)
                else:
                    p.income3 = self.set_income3_by_rank(quartiles_group3, p.nt3_rank-1)
                p.participant.vars['income3'] = p.income3
                p.participant.vars['income3'] = p.income3
        self.set_round_group()
# set the decsion group for all 7 rounds
# find the median of nt3_dif
# set rd1, ..., rd7
# set rd1a and rd1b among rd1, .., rd7

    def set_round_group(self):

        group800 = [[p.id,p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['income3'] == 800]
        group600 = [[p.id,p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['income3'] == 600]
        group400 = [[p.id,p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['income3'] == 400]
        group200 = [[p.id,p.participant.vars['nt3_points']] for p in self.get_players() if p.participant.vars['income3'] == 200]


        nt3_dif_lst = []
        rd_period3 = []
        for r in range(0,7):
            rd_period3.append([random.sample([800, 400, 600, 200], k=1)[0]
                               for num_g in range(0,len(self.get_players())//4)])
        rd1a_period3 = random.randint(1, 7)
        rd1b_period3 = random.randint(1, 7)

        assert(len(group800) == len(group600) == len(group400) == len(group200))
        for i in range(0, Constants.num_rounds):
            random.shuffle(group800)
            random.shuffle(group600)
            random.shuffle(group400)
            random.shuffle(group200)

            difs = [group400[x][1] - group200[x][1] for x in range(0, len(group400))]
            for dif in difs:
                nt3_dif_lst.append(dif)
            group800_pid = [pair[0] for pair in group800]
            group600_pid = [pair[0] for pair in group600]
            group400_pid = [pair[0] for pair in group400]
            group200_pid = [pair[0] for pair in group200]

            for p in self.get_players():
                if i == 0:
                    p.participant.vars['decgroup_period3'] = []
                    p.participant.vars['rd_period3'] = rd_period3
                    p.participant.vars['rd2_period3'] = [rd1a_period3, rd1b_period3]
                if p.income3 == 800:
                    p.participant.vars['decgroup_period3'].append(group800_pid.index(p.id)+1)
                if p.income3 == 600:
                    p.participant.vars['decgroup_period3'].append(group600_pid.index(p.id)+1)
                if p.income3 == 400:
                    p.participant.vars['decgroup_period3'].append(group400_pid.index(p.id)+1)
                if p.income3 == 200:
                    p.participant.vars['decgroup_period3'].append(group200_pid.index(p.id)+1)

        nt_dif_median = np.median(nt3_dif_lst)
        for p in self.get_players():
            p.participant.vars['nt3_dif_median'] = nt_dif_median
            print("decgroup order: ", p.participant.vars['decgroup_period3'])
        print("nt dif median: ", nt_dif_median)

    def set_rg_tokens(self):
        for r in range(0,7):
            for p in self.get_players():
                cur_decgroup = p.participant.vars['decgroup_period3'][r]
                cur_rd = p.participant.vars['rd_period3'][r][cur_decgroup-1]
                cur_dv = None
                tokens = 0
                cur_comp = p.participant.vars['competition_period3'][r]
                if p.income3 == 400 and cur_comp == 1:
                    tokens -= 40
                if p.income3 == cur_rd:
                    cur_dv = p.participant.vars['dv_period3'][r]
                    if cur_dv == 1:
                        tokens = p.income3 - p.income3 * 0.2 + 100
                    if cur_dv == 2:
                        tokens = p.income3 - p.income3 * 0.4 + 200
                else:
                    for q in p.get_others_in_subsession():
                        if cur_decgroup == q.participant.vars['decgroup_period3'][r]:
                            if q.income3 == cur_rd:
                                cur_dv = q.participant.vars['dv_period3'][r]
                                if cur_dv == 1:
                                    tokens = p.income3 - p.income3 * 0.2 + 100
                                if cur_dv == 2:
                                    tokens = p.income3 - p.income3 * 0.4 + 200
                                break
                p.participant.vars['rg_tokens_period3'].append(tokens)
        for p in self.get_players():
            p.rg1_tokens = p.participant.vars['rg_tokens_period3'][0]
            p.rg2_tokens = p.participant.vars['rg_tokens_period3'][1]
            p.rg3_tokens = p.participant.vars['rg_tokens_period3'][2]
            p.rg4_tokens = p.participant.vars['rg_tokens_period3'][3]
            p.rg5_tokens = p.participant.vars['rg_tokens_period3'][4]
            p.rg6_tokens = p.participant.vars['rg_tokens_period3'][5]
            p.rg7_tokens = p.participant.vars['rg_tokens_period3'][6]

    def set_rgab_tokens(self):
        for p in self.get_players():
            rd1a = p.participant.vars['rd2_period3'][0]
            rd1b = p.participant.vars['rd2_period3'][1]
            p.participant.vars['period3_payoff'] = p.participant.vars['rg_tokens_period3'][rd1a-1] \
                                                  + p.participant.vars['rg_tokens_period3'][rd1b-1]


class Player(BasePlayer):
    pt_group_id = models.StringField()
    income3 = models.IntegerField()
    nt3_rank = models.IntegerField()

    decgroup = models.IntegerField()
    nt_dif = models.IntegerField()
    competition = models.IntegerField()
    nt_dif_median = models.IntegerField()

    dv = models.IntegerField(widget=widgets.RadioSelect)
    rd = models.IntegerField()
    rd1a_period3 = models.IntegerField()
    rd1b_period3 = models.IntegerField()

    rg1_tokens = models.FloatField()
    rg2_tokens = models.FloatField()
    rg3_tokens = models.FloatField()
    rg4_tokens = models.FloatField()
    rg5_tokens = models.FloatField()
    rg6_tokens = models.FloatField()
    rg7_tokens = models.FloatField()

    def set_nt3_points(self):
        self.nt3_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt3_points -= 10
        self.participant.vars['nt3_points'] = self.nt3_points

    def set_info(self, round_var):
        self.decgroup = self.participant.vars['decgroup_period3'][round_var-1]
        print("player: ", self.id_in_group, ' ', self.decgroup, " group lst: ", self.participant.vars['decgroup_period3'])
        self.income3 = self.participant.vars['income3']
        self.rd = self.participant.vars['rd_period3'][round_var-1][self.decgroup-1]
        self.rd1a_period3 = self.participant.vars['rd2_period3'][0]
        self.rd1b_period3 = self.participant.vars['rd2_period3'][1]

        self.pt_group_id = ['Klee-Bazille', 'Klee-Boch', 'Kandinksy-Boch'][self.participant.vars['pt_group_id'] - 1]

# Find the group memebers' information [income3, group_id]
# Compare dif of this round: token 400's raw pts - token 200's raw pts > dif median?

    def find_group_members_info(self, round_var):
        result = []
        dif = 0
        group_id_400token = ''

        if self.income3 == 400:
            dif += self.participant.vars['nt3_points']
            group_id_400token = self.pt_group_id
        if self.income3 == 200:
            dif -= self.participant.vars['nt3_points']
        for other in self.get_others_in_subsession():
            if other.participant.vars['decgroup_period3'][round_var-1] == self.decgroup:
                income = other.participant.vars['income3']
                result.append([['Klee-Bazille', 'Klee-Boch', 'Kandinksy-Boch'][other.participant.vars['pt_group_id']-1],
                               income,
                               other.participant.vars['nt3_points']])
                # Define the dif in this dec group
                if income == 400:
                    dif += other.participant.vars['nt3_points']
                    group_id_400token = ['Klee-Bazille', 'Klee-Boch', 'Kandinksy-Boch'][other.participant.vars['pt_group_id']-1]
                if income == 200:
                    dif -= other.participant.vars['nt3_points']

        self.nt_dif = dif
        random.shuffle(result)
        print("members: ", result)
        print("result dif: ", dif)
        print("group median: ", self.participant.vars['nt3_dif_median'])
        return [result, group_id_400token]

    def set_competition(self):
        if self.nt_dif > self.participant.vars['nt3_dif_median']:
            self.competition = 0
        else:
            self.competition = 1
        self.participant.vars['competition_period3'].append(self.competition)
