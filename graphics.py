import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


def draw_text(screen, text, textcolor, rect_color, x, y, text_size):
    font = pygame.font.SysFont('DS Crystal', text_size)
    text = font.render(text, True, textcolor, rect_color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
