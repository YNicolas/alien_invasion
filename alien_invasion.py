#!/user/bin/python3
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as game_func


def run_game():
    #  Initialize game & creat a screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("The War of Bee")

    stats = GameStats(ai_settings)
    score_b = Scoreboard(ai_settings, screen, stats)

    button_play = Button(ai_settings, screen, "Play")
    # creat a ship
    ship = Ship(ai_settings, screen)

    bullets = Group()
    # creat aline
    aliens = Group()

    game_func.creat_fleet(ai_settings, screen, ship, aliens)
    # start game loop
    while True:
        # Monitor keyboard and mouse events
        game_func.check_events(ai_settings, screen, stats, score_b, button_play, ship, aliens, bullets)
        if stats.game_active:
            # move the ship
            ship.update()

            # check the state of bullets
            game_func.update_bullets(ai_settings, screen, stats, score_b, ship, aliens, bullets)
            # print(len(bullets))

            # update alien
            game_func.update_aliens(ai_settings, stats, score_b, screen, ship, aliens, bullets)

        game_func.update_screen(ai_settings, screen, stats, score_b, ship, aliens, bullets, button_play)


run_game()
