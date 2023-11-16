import pygame
import random
import time
import settings
import json


class Score(pygame.sprite.Sprite):
    def __init__(self, score=0, x=settings.SCREEN_WIDTH - 3 * settings.TILE_SIZE, y=0):
        super().__init__()
        # counters
        self.score = score
        self.highscore = self.load_high_score()
        self.score_font = pygame.font.Font('assets/fonts/score.ttf', 30)
        self.highscore_msg = self.score_font.render(str(self.highscore), True, (176, 209, 224))
        self.score_msg = self.score_font.render(str(self.score), True, (176, 209, 224))

        # score box
        self.image = pygame.image.load('assets/images/score_counter.PNG').convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def load_high_score(self):
        file_path = 'assets/score_log/highscore.json'
        try:
            with open(file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            # If the file is not found (first run or deleted), return 0
            return 0

    def update_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file_path = 'assets/score_log/highscore.json'
            with open(file_path, 'w') as json_file:
                json.dump(self.highscore, json_file)
            print(f'the highscore is now {self.highscore}')

    def update_score_text(self):
        self.score_msg = self.score_font.render(str(self.score), True, (176, 209, 224))
    def update_highscore_text(self):
        self.highscore_msg = self.score_font.render(str(self.highscore), True, (176, 209, 224))
    def update(self):
        # font
        self.score += 1
        self.image = self.image
        print(self.score)
