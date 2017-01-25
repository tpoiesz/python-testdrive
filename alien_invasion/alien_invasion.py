import pygame
import sys

from settings import Settings


def game_init():

    pygame.init()

    i_settings = Settings()
    screen = pygame.display.set_mode(
        (i_settings.screen_width, i_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(i_settings.bg_color)

        pygame.display.flip()


game_init()
