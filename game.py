class Game(object):
    def __init__(self, game_over, coins, coin_per_click, cost_upgrade,
                 cost_auto_first, cost_auto_second):
        self.game_over = game_over
        self.coins = coins
        self.coin_per_click = coin_per_click
        self.cost_upgrade = cost_upgrade
        self.cost_auto_first = cost_auto_first
        self.cost_auto_second = cost_auto_second
        self.auto_click = 0

    def upgrade(self):
        self.coins -= self.cost_upgrade
        self.cost_upgrade *= 2
        self.coin_per_click *= 1.25

    def auto_first(self):
        self.coins -= self.cost_auto_first
        self.cost_auto_first *= 2
        self.auto_click += 0.005

    def auto_second(self):
        self.coins -= self.cost_auto_second
        self.cost_auto_second *= 2
        self.auto_click += 0.0025

    def click(self):
        self.coins += self.coin_per_click

    def central_click(self):
        self.coins += 1.1 * self.coin_per_click

    def auto_mine(self):
        self.coins += self.auto_click
