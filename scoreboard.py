import pygame.font


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highest_score()
        self.prep_level()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prep_highest_score(self):
        highest_score_str = str(self.stats.highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.highest_score_image_rect = self.highest_score_image.get_rect()
        self.highest_score_image_rect.centerx = self.screen_rect.centerx
        self.highest_score_image_rect.top = self.score_image_rect.top

    def prep_level(self):
        self.level_str = str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True, self.text_color, self.ai_settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)

