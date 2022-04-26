import pygame
import game


def main_loop():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((game.width, game.height))
    pygame.display.set_caption("Clicker")
    game_logic = game.Game(True, 0, 1, 10, 2)
    while game_logic.game_over:
        game_logic.events()
        game_logic.draw(screen)
        pygame.display.update()
        clock.tick(120)
    quit()


if __name__ == '__main__':
    main_loop()
