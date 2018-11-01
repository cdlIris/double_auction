from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Market(Page):
    timeout_seconds = Constants.time_per_round

    def vars_for_template(self):
        c = self.player.get_form_context()
        c['asks'] = self.group.get_asks()
        c['bids'] = self.group.get_bids()
        c['repository'] = self.player.get_repo_context()
        return c


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Market,
    ResultsWaitPage,
    Results
]
