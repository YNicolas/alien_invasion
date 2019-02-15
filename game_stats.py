import json


class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.load_highest_score()
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0

    def load_highest_score(self):
        filename = "highest_score.json"
        try:
            with open(filename) as f_read:
                self.highest_score = json.load(f_read)
                print(self.highest_score)
        except FileNotFoundError:
            self.highest_score = 0
            with open(filename, "w") as f_c:
                json.dump(str(self.highest_score), f_c)

    def dump_highest_score(self):
        filename = "highest_score.json"
        with open(filename, "w") as f_obj:
            print(self.highest_score)
            json.dump(self.highest_score, f_obj)
