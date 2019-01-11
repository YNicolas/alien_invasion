#!/user/bin/python3
import pygame

from settings import Settings
from ship import Ship
import game_functions as game_func


def run_game():
    #  Initialize game & creat a screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # creat a ship
    ship = Ship(screen)

    # start game loop
    while True:
        # Monitor keyboard and mouse events
        game_func.check_events()

        # Refresh screen
        # set the background color
        # ship
        game_func.update_screen(ai_settings, screen, ship)


run_game()
