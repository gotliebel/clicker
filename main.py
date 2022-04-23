import sys
import pygame
import game
import graphics

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
    game_logic = game.Game(True, 0, 1, 10)
    while game_logic.game_over:
        game_logic.auto_click()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                game_logic.game_over = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                game_logic.game_over = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    game_logic.browse_event(mouse_position)
        if game_logic.coins >= sys.maxsize:
            print("Congratulations!")
            game_logic.game_over = False

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
        graphics.draw_text(screen, "Upgrade click " + str(round(game_logic.cost_upgrade, 2)), black, aqua, 500, 530, 30)
        graphics.draw_text(screen, "Buy strong auto miner " + str(round(game.first_auto_clicker.cost, 2)), black, aqua,
                           150, 370, 30)
        graphics.draw_text(screen, "You have " + str(int(game_logic.coins)) + " coins", black, aqua, width // 2, 50, 30)
        graphics.draw_text(screen, "You gain " + str(round(game_logic.coin_per_click, 2)) + " coins per click", black,
                           aqua, width // 2 - 300, 80, 30)
        graphics.draw_text(screen, "You mine " +
                           str(round(120 * (game.first_auto_clicker.auto + game.second_auto_clicker.auto), 2)) +
                           " coins per second", black, aqua, width // 2 + 300, 80, 30)
        graphics.draw_text(screen, "Buy weak auto miner  " + str(round(game.second_auto_clicker.cost, 2)), black, aqua,
                           850, 370, 30)
        pygame.display.update()
        clock.tick(120)
    quit()


if __name__ == '__main__':
    main_loop()
