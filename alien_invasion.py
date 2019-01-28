#!/user/bin/python3
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as game_func


def run_game():
    #  Initialize game & creat a screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("The War of Bee")

    # creat a ship
    ship = Ship(ai_settings, screen)

    bullets = Group()
    # creat aline
    aliens = Group()

    game_func.creat_fleet(ai_settings, screen, aliens)
    # start game loop
    while True:
        # Monitor keyboard and mouse events
        game_func.check_events(ai_settings, screen, ship, bullets)
        # move the ship
        ship.update()

        # check the state of bullets
        game_func.update_bullets(bullets)
        # print(len(bullets))

        # update alien
        game_func.update_aliens(ai_settings, aliens)
        game_func.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
