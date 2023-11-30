import pygame
import time
import random
import settings


class Stardust(pygame.sprite.Sprite):
    def __init__(self, x=200, y=200):
        super().__init__()
        self.image = pygame.image.load('assets/images/coin.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(x,y,self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if self.moving_left:
            self.rect.x -= 1
        if self.rect.right <= 0:
            self.rect.x = settings.SCREEN_WIDTH + 2*settings.TILE_SIZE
            self.rect.y = (random.randint(0, settings.SCREEN_HEIGHT - 2*settings.TILE_SIZE))
    def reset(self):
        self.kill()
stardusts = pygame.sprite.Group()