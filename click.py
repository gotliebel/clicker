import pygame
import time

pygame.init()

clock = pygame.time.Clock()
auto_click = 0
coins = 0
coins_by_miner = 0
width = 1000
height = 800
black = (0, 0, 0)
blue = (0, 100, 250)
aqua = (0, 255, 255)
purple = (128, 0, 128)
gold = (255, 215, 0)
yellow = (255, 235, 59)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clicker")


def autominer():
    global coins_by_miner
    global coins
    global auto_click
    time.sleep(0.1)
    coins += auto_click
    coins_by_miner += auto_click


def DrawText(text, textcolor, rect_color, x, y, text_size):
    font = pygame.font.SysFont('DS Crystal', text_size)
    text = font.render(text, True, textcolor, rect_color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


cl = Button(width // 2, height // 2, 'click.png')


def main_loop():
    global auto_click
    global coins_by_miner
    global coins
    coin_per_click = 1
    cost_auto = 10
    cost_upgrade = 10
    game_running = True
    while game_running:
        if game_running:
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                mouse_presses = pygame.mouse.get_pressed()
                if (mouse_position[0] - width // 2) * (
                        mouse_position[0] - width // 2) + (
                        mouse_position[1] - height // 2) * (
                        mouse_position[1] - height // 2) <= 13 * 13 and \
                        mouse_presses[0]:
                    coins += coin_per_click * 2
                elif (mouse_position[0] - width // 2) * (
                        mouse_position[0] - width // 2) + (
                        mouse_position[1] - height // 2) * (
                        mouse_position[1] - height // 2) <= 100 * 100 and \
                        mouse_presses[0]:
                    coins += coin_per_click

                if mouse_position >= (700, 400) and mouse_presses[0]:
                    if mouse_position <= (1000, 800):
                        if coins >= cost_upgrade:
                            coins -= cost_upgrade
                            cost_upgrade *= 2
                            coin_per_click *= 2

                if mouse_position >= (0, 400) and mouse_presses[0]:
                    if mouse_position <= (300, 800):
                        if coins >= cost_auto:
                            coins -= cost_auto
                            cost_auto *= 2
                            auto_click = 1

        if coins >= 1234567890987:
            print("Congratulations!")
            game_running = False

        if coins_by_miner >= cost_auto * 3 // 4:
            auto_click = 0
            coins_by_miner = 0

        screen.fill(aqua)
        DrawText("Click this button", gold, aqua, width // 2,
                 height // 2 - 300, 50)
        pygame.draw.polygon(screen, gold,
                            [(480, 113), (480, 250), (460, 250), (500, 300),
                             (540, 250), (520, 250), (520, 113)])
        DrawText("You have " + str(coins) + " coins", black,
                 aqua, width // 2, 50, 30)
        DrawText("Upgrade click " + str(cost_upgrade), black, aqua,
                 850, 370,
                 30)
        DrawText("Buy auto miner " + str(cost_auto), black, aqua, 150,
                 370,
                 30)
        pygame.draw.rect(screen, purple, (0, 400, 300, 400), 0, 0, 10, 10, 0,
                         10)
        pygame.draw.rect(screen, purple, (700, 400, 1000, 400), 0, 0, 10, 10,
                         10, 0)
        screen.blit(cl.image, cl.rect)
        DrawText("Click me", black, yellow, width // 2, height // 2 - 50, 40)
        pygame.display.update()
        clock.tick(120)


main_loop()
pygame.quit()
quit()
