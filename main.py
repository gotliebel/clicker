import pygame
import sys
import graphics
from game import Game

width = 1000
height = 800
black = (0, 0, 0)
blue = (0, 100, 250)
aqua = (0, 255, 255)
purple = (128, 0, 128)
gold = (255, 215, 0)
yellow = (255, 235, 59)


def main_loop():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Clicker")
    game = Game(True, 0, 1, 10, 10, 5)
    while game.game_over:
        game.auto_mine()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game.game_over = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                mouse_presses = pygame.mouse.get_pressed()
                if (mouse_position[0] - width // 2) * (
                        mouse_position[0] - width // 2) + (
                        mouse_position[1] - height // 2) * (
                        mouse_position[1] - height // 2) <= 13 * 13 and \
                        mouse_presses[0]:
                    game.central_click()
                elif (mouse_position[0] - width // 2) * (
                        mouse_position[0] - width // 2) + (
                        mouse_position[1] - height // 2) * (
                        mouse_position[1] - height // 2) <= 100 * 100 and \
                        mouse_presses[0]:
                    game.click()
                if mouse_position[0] >= 400 and mouse_position[1] >= 550 and \
                        mouse_presses[0]:
                    if mouse_position[0] <= 600 and mouse_position[1] <= 800:
                        if game.coins >= game.cost_upgrade:
                            game.upgrade()
                if mouse_position[0] >= 0 and mouse_position[1] >= 400 and \
                        mouse_presses[0]:
                    if mouse_position[0] <= 300 and mouse_position[1] <= 800:
                        if game.coins >= game.cost_auto_first:
                            game.auto_first()
                if mouse_position[0] >= 700 and mouse_position[1] >= 400 and \
                        mouse_presses[0]:
                    if mouse_position[0] <= 1000 and mouse_position[1] <= 800:
                        if game.coins >= game.cost_auto_second:
                            game.auto_second()
        if game.coins >= sys.maxsize:
            print("Congratulations!")
            game.game_over = False

        screen.fill(aqua)
        pygame.draw.polygon(screen, gold,
                            [(480, 113), (480, 250), (460, 250), (500, 300),
                             (540, 250), (520, 250), (520, 113)])
        pygame.draw.rect(screen, purple, (700, 400, 300, 400), 0, 0, 10, 10,
                         10, 0)
        pygame.draw.rect(screen, purple, (0, 400, 300, 400), 0, 0, 10, 10, 0,
                         10)
        pygame.draw.rect(screen, purple, (400, 550, 200, 250), 0, 0, 10, 10,
                         10, 10)
        screen.blit(
            graphics.Button(width // 2, height // 2, 'click.png').image,
            graphics.Button(width // 2, height // 2, 'click.png').rect)
        graphics.draw_text(screen, "Click this button", gold, aqua, width // 2,
                           height // 2 - 300, 50)
        graphics.draw_text(screen, "Click me", black, yellow, width // 2,
                           height // 2 - 50, 40)
        graphics.draw_text(screen,
                           "Upgrade click " + str(round(game.cost_upgrade, 2)),
                           black,
                           aqua,
                           500,
                           530,
                           30)
        graphics.draw_text(screen,
                           "Buy strong auto miner " + str(
                               round(game.cost_auto_first, 2)),
                           black, aqua, 150,
                           370,
                           30)
        graphics.draw_text(screen,
                           "You have " + str(int(game.coins)) + " coins",
                           black,
                           aqua, width // 2, 50, 30)
        graphics.draw_text(screen,
                           "You gain " + str(
                               round(game.coin_per_click,
                                     2)) + " coins per click",
                           black,
                           aqua, width // 2 - 300, 80, 30)
        graphics.draw_text(screen,
                           "You mine " + str(
                               round(120 * game.auto_click,
                                     2)) + " coins per second",
                           black,
                           aqua, width // 2 + 300, 80, 30)
        graphics.draw_text(screen,
                           "Buy weak auto miner  " + str(
                               round(game.cost_auto_second, 2)),
                           black, aqua,
                           850, 370,
                           30)
        pygame.display.update()
        clock.tick(120)
    pygame.quit()


if __name__ == '__main__':
    main_loop()
