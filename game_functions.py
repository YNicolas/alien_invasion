import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        stats.dump_highest_score()
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, score_b, button_play, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.dump_highest_score()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score_b, button_play, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, score_b, ship, aliens, bullets, button_play):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    score_b.show_score()
    if not stats.game_active:
        button_play.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, score_b, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, score_b, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, score_b, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score_b.prep_score()
            check_highest_score(stats, score_b)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        score_b.prep_level()
        creat_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def creat_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    print(number_rows)
    for row_number in range(number_rows):
        for alien_number_x in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number_x, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number_x, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number_x
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def update_aliens(ai_settings, stats, score_b, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score_b, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, score_b, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, score_b, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        score_b.prep_ships()
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(1)
    else:
        print("Game over!!!")
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, score_b, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, score_b, screen, ship, aliens, bullets)
            break


def check_play_button(ai_settings, screen, stats, score_b, button_play, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = button_play.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        score_b.prep_score()
        score_b.prep_highest_score()
        score_b.prep_level()
        score_b.prep_ships()

        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_highest_score(stats, score_b):
    if stats.score > stats.highest_score:
        stats.highest_score = stats.score
        score_b.prep_highest_score()

