class Autoclicker(object):
    def __init__(self, cost_miner):
        self.cost = cost_miner
        self.auto = 0

    def upgrade_miner(self, coin):
        self.cost *= 2
        self.auto += coin

    def auto_mine(self):
        return self.auto
