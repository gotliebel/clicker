from autoclicker import Autoclicker
import pygame
import sys
import graphics

width = 1000
height = 800
black = (0, 0, 0)
blue = (0, 100, 250)
aqua = (0, 255, 255)
purple = (128, 0, 128)
gold = (255, 215, 0)
yellow = (255, 235, 59)


class Game(object):
    list_auto_clicker = []

    def __init__(self, game_over, coins, coin_per_click, cost_upgrade, number_auto_clickers):
        self.game_over = game_over
        self.coins = coins
        self.coin_per_click = coin_per_click
        self.cost_upgrade = cost_upgrade
        self.auto = 0
        self.number_auto_clickers = number_auto_clickers
        for i in range(5, 5 * self.number_auto_clickers + 1, 5):
            self.add_auto_clicker(Autoclicker(i))

    def events(self):
        self.auto_click()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.game_over = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                self.game_over = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    self.browse_event(mouse_position)
        if self.coins >= sys.maxsize:
            print("Congratulations!")
            self.game_over = False

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
            if self.coins >= self.list_auto_clicker[1].cost:
                self.coins -= self.list_auto_clicker[1].cost
                self.list_auto_clicker[1].upgrade_miner(0.005)
        if 700 <= position[0] <= 1000 and 400 <= position[1] <= 800:
            if self.coins >= self.list_auto_clicker[0].cost:
                self.coins -= self.list_auto_clicker[0].cost
                self.list_auto_clicker[0].upgrade_miner(0.0025)

    def draw(self, screen):
        screen.fill(aqua)
        pygame.draw.polygon(screen, gold,
                            [(480, 113), (480, 250), (460, 250), (500, 300), (540, 250), (520, 250), (520, 113)])
        pygame.draw.rect(screen, purple, (700, 400, 300, 400), 0, 0, 10, 10, 10, 0)
        pygame.draw.rect(screen, purple, (0, 400, 300, 400), 0, 0, 10, 10, 0, 10)
        pygame.draw.rect(screen, purple, (400, 550, 200, 250), 0, 0, 10, 10, 10, 10)
        screen.blit(graphics.Button(width // 2, height // 2, 'click.png').image,
                    graphics.Button(width // 2, height // 2, 'click.png').rect)
        graphics.draw_text(screen, "Click this button", gold, aqua, width // 2, height // 2 - 300, 50)
        graphics.draw_text(screen, "Click me", black, yellow, width // 2, height // 2 - 50, 40)
        graphics.draw_text(screen, "Upgrade click " + str(round(self.cost_upgrade, 2)), black, aqua, 500, 530, 30)
        graphics.draw_text(screen, "Buy strong auto miner " + str(round(self.list_auto_clicker[1].cost, 2)), black,
                           aqua,
                           150, 370, 30)
        graphics.draw_text(screen, "You have " + str(int(self.coins)) + " coins", black, aqua, width // 2, 50, 30)
        graphics.draw_text(screen, "You gain " + str(round(self.coin_per_click, 2)) + " coins per click", black,
                           aqua, width // 2 - 300, 80, 30)
        graphics.draw_text(screen, "You mine " +
                           str(round(120 * (self.list_auto_clicker[0].auto + self.list_auto_clicker[1].auto), 2)) +
                           " coins per second", black, aqua, width // 2 + 300, 80, 30)
        graphics.draw_text(screen, "Buy weak auto miner  " + str(round(self.list_auto_clicker[0].cost, 2)), black, aqua,
                           850, 370, 30)

    def upgrade(self):
        self.coins -= self.cost_upgrade
        self.cost_upgrade *= 2
        self.coin_per_click *= 1.25

    def click(self):
        self.coins += self.coin_per_click

    def central_click(self):
        self.coins += 1.1 * self.coin_per_click

    def add_auto_clicker(self, auto_clicker):
        self.list_auto_clicker.append(auto_clicker)

    def auto_click(self):
        for i in range(self.number_auto_clickers):
            self.coins += self.list_auto_clicker[i].auto_mine()
