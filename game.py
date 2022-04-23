from autoclicker import Autoclicker

width = 1000
height = 800

first_auto_clicker = Autoclicker(10)
second_auto_clicker = Autoclicker(5)


class Game(object):
    def __init__(self, game_over, coins, coin_per_click, cost_upgrade):
        self.game_over = game_over
        self.coins = coins
        self.coin_per_click = coin_per_click
        self.cost_upgrade = cost_upgrade
        self.auto = 0

    def browse_event(self, position):
        if (position[0] - width // 2) * (position[0] - width // 2) + (position[1] - height // 2) * \
                (position[1] - height // 2) <= 13 * 13:
            self.central_click()
        elif (position[0] - width // 2) * (position[0] - width // 2) + (position[1] - height // 2) * (
                position[1] - height // 2) <= 100 * 100:
            self.click()
        if 400 <= position[0] <= 600 and 550 <= position[1] <= 800:
            if self.coins >= self.cost_upgrade:
                self.upgrade()
        if 0 <= position[0] <= 300 and 400 <= position[1] <= 800:
            if self.coins >= first_auto_clicker.cost:
                self.coins -= first_auto_clicker.cost
                first_auto_clicker.upgrade_miner(0.005)
        if 700 <= position[0] <= 1000 and 400 <= position[1] <= 800:
            if self.coins >= second_auto_clicker.cost:
                self.coins -= second_auto_clicker.cost
                second_auto_clicker.upgrade_miner(0.0025)

    def upgrade(self):
        self.coins -= self.cost_upgrade
        self.cost_upgrade *= 2
        self.coin_per_click *= 1.25

    def click(self):
        self.coins += self.coin_per_click

    def central_click(self):
        self.coins += 1.1 * self.coin_per_click

    def auto_click(self):
        self.coins += first_auto_clicker.auto_mine()
        self.coins += second_auto_clicker.auto_mine()
