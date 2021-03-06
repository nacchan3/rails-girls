from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    def is_displayed(self):
        return self.round_number == 1


class student(Page):


    form_model = models.Player
    form_fields = ['student_first_choice',
                   'student_second_choice',
                   'student_third_choice',
                   'student_fourth_choice'
                   ]

#重複チェック
    def error_message(self,values):
        if values["student_first_choice"] == values["student_second_choice"]:
            return '第一希望と第二希望が重複しています。'
        elif values["student_first_choice"] == values["student_third_choice"]:
            return '第一希望と第三希望が重複しています。'
        elif values["student_first_choice"] == values["student_fourth_choice"]:
            return '第一希望と第四希望が重複しています。'
        elif values["student_second_choice"] == values["student_third_choice"]:
            return '第二希望と第三希望が重複しています。'
        elif values["student_second_choice"] == values["student_fourth_choice"]:
            return '第二希望と第四希望が重複しています。'
        elif values["student_third_choice"] == values["student_fourth_choice"]:
            return '第三希望と第四希望が重複しています。'



class ResultsWaitPage2(WaitPage):
    def after_all_players_arrive(self):
        self.group.tekitou2()


class Results(Page):
    timer_text = '30秒後に次のラウンドが始まります。'
    timeout_seconds = 30

    pass




page_sequence = [
    MyPage,
    student,
    ResultsWaitPage2,
    Results
]
