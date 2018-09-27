from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'
class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    age = [i for i in range(16, 100)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1 = models.IntegerField(
        label='What is your age?',
        choices=Constants.age)

    q2 = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    q3 = models.StringField(
        choices=['Yes', 'No'],
        label='Have you participated in Economics or Psychology experiments before?',
        widget=widgets.RadioSelect
    )

    q4 = models.StringField(
        choices=['Humanities','Mathematical', 'Physical, and Life Sciences','Medical Sciences',
                 'Economics or PPE (Politics, Philosophy, and Economics)','Other Social Sciences '],
        label='Field of study:',
        widget=widgets.RadioSelect
    )
    q5 = models.StringField(
        choices=['Graduate', 'Undergraduate'],
        label='Degree:',
        widget=widgets.RadioSelect
    )
    q6 = models.StringField(
        choices=['1','2','3','4','5+'],
        label = 'Which year are you in your program?'
    )
    q7 = models.StringField(
        choices=['0 (I avoid taking risks)', '1','2','3','4','5','6','7','8','9', '10 (I take risks)'],
        label='How do you see yourself: Are you in general a person who takes risks or do you try to avoid taking risks?',
        widget=widgets.RadioSelectHorizontal
    )
    q8 = models.StringField(
        label='Generally speaking, would you say that most people can be trusted or that you can’t be too careful in dealing with people?',
        choices =['0 (You can’t be too careful)', '1','2','3','4','5','6','7','8','9', '10 (Most people can be trusted) '],
        widget=widgets.RadioSelectHorizontal
    )
    q9 = models.StringField(
        label='To what extent do you agree with the following statement: “If I help someone I expect some help in return”.',
        choices= ['Agree strongly','Agree','Neither agree nor disagree','Disagree','Disagree strongly '],
        widget=widgets.RadioSelect
    )
    q10=models.StringField(
        label='To what extent do you agree with the following statement: “It is important that every person in the world should be treated equally. Everyone should have equal opportunities in life.”',
        choices=['Agree strongly','Agree','Neither agree nor disagree','Disagree','Disagree strongly '],
        widget=widgets.RadioSelect
    )
    q11=models.StringField(
        label='Some people think that the government ought to reduce the income differences between the rich and the poor,'
              ' perhaps by raising the taxes of wealthy families or by giving income assistance to the poor. Others think '
              'that the government should not concern itself with reducing this income difference between the rich and the poor.'
              ' Here is a card with a scale from 1 to 7. Think of a score of 1 as meaning that the government ought to reduce the'
              ' income differences between rich and poor, and a score of 7 meaning that the government should not concern itself with '
              'reducing income differences. What score between 1 and 7 comes closest to the way you feel?',
        choices=['1 (Government ought to reduce income differences) ', '2','3','4','5','6', '7 (Government should not concern itself with reducing income differences)'],
        widget=widgets.RadioSelectHorizontal
    )
    q12=models.StringField(
        label='Many social benefits and services are paid for by taxes. If the government had to choose between '
              'increasing taxes and spending more on social benefits and  services, or decreasing taxes and spending '
              'less on social benefits and services, which  should they do? ',
        choices=['0 (Government should decrease taxes a lot and spend much less on social benefits and services) ',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (Government should increase taxes a lot and spend much more on social benefits and services)'],
        widget=widgets.RadioSelectHorizontal
    )
    q13=models.StringField(
        label='In politics people sometimes talk of “left” and “right”. Where would you place yourself on this scale, where 0 means the left and 10 means the right?',
        choices=['0 (left)', '1','2','3','4','5','6','7','8','9', '10 (right)'],
        widget=widgets.RadioSelectHorizontal
    )
    q14=models.StringField(
        label='You were assigned to the ________ group during the experiment.',
        choices=['Klee-Bazille','Kandinsky-Boch','Klee-Boch'],
        widget=widgets.RadioSelect
    )
    q15=models.StringField(
        label='On a scale from 1 (Not at all) to 7 (Very much), how strongly did you feel belongingness to the your group?',
        choices = ['0', '1','2','3','4','5','6','7'],
        widget = widgets.RadioSelect
    )
    q16 = models.StringField(
        label='On a scale from 1 (Not at all) to 7 (Very much), how much commonality did you think you shared with the members in your group? ',
        choices=['0', '1','2','3','4','5','6','7'],
        widget=widgets.RadioSelect
    )
    q17 = models.StringField(
        label='On a scale from 1 (Not at all) to 7 (Very much), how close did you feel toward members in your group?',
        choices=['0', '1', '2', '3', '4', '5', '6', '7'],
        widget=widgets.RadioSelect
    )
    q18 = models.StringField(
        label='On a scale from 1 (Not at all) to 7 (Very much), how favorably did you feel toward the members in your group? ',
        choices=['0', '1', '2', '3', '4', '5', '6', '7'],
        widget=widgets.RadioSelect
    )
    other = models.StringField(label='If you select other option. Please specify', widget=widgets.TextInput,blank=True)
    q19 = models.StringField(
        label='In Part 2 you were asked to choose your preferred tax and transfer scheme. How would you describe the strategy you used?',
        choices=['Try to maximize my number of tokens.','Try to maximize the number of tokens for the entire group.',
                 'Try to maximize the number of tokens for the poorest group member.', 'Other.Please specify'],
        widget=widgets.RadioSelect
    )
    q20a=models.StringField(
        label='Which participant pays the highest amount of taxes in absolute terms?',
        widget=widgets.TextInput
    )
    q20b=models.StringField(
        label='Which participant benefits the most in absolute terms from this scheme?',
        widget=widgets.TextInput
    )
    q20c = models.StringField(
        label='What is the total sum of taxes paid by participants?',
    widget = widgets.TextInput
    )
    q21=models.StringField(
        label='What do you think the experiment was about?',
        widget=widgets.TextInput()
    )
    klee =models.StringField(
        label='Klee',
        choices=['1 (Very familiar)', '2','3','4','5','6','7','8','9', '10 (Not at all familiar)'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    kandinsky = models.StringField(
        label='Kandinsky',
        choices=['1 (Very familiar)', '2','3','4','5','6','7','8','9', '10 (Not at all familiar)'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    boch = models.StringField(
        label='Boch',
        choices=['1 (Very familiar)', '2','3','4','5','6','7','8','9', '10 (Not at all familiar)'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    bazille = models.StringField(
        label='Bazille',
        choices=['1 (Very familiar)', '2','3','4','5','6','7','8','9', '10 (Not at all familiar)'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    q22=models.StringField(
        label='On a scale from 1 to 10, please rate how familiar you were with the paintings made by ____ before this experiment.',
        widget=widgets.RadioSelect,
        choices = ['Klee','Kandinsky','Boch','Bazille'],
        blank=True
    )

