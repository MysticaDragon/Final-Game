import pygame
import random
import time
import settings


class Dragon(pygame.sprite.Sprite):
    def __init__(self, x=200, y=200):
        super().__init__()
        self.right_image = pygame.image.load('assets/images/pink_fish_rest.png').convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        self.rect = pygame.rect.Rect(x,y,self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def reset_position(self):
        self.x = 200
        self.y = 200
    def update(self):

        if self.moving_left:
            self.rect.x -= 2
            self.image = self.left_image

        elif self.moving_right:
            self.rect.x += 2
            self.image = self.right_image
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 4

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x >= settings.SCREEN_WIDTH - 2*settings.TILE_SIZE:
            self.rect.x = settings.SCREEN_WIDTH  - 2*settings.TILE_SIZE
        if self.rect.y >= settings.SCREEN_HEIGHT  - settings.TILE_SIZE:
            self.rect.y = settings.SCREEN_HEIGHT - settings.TILE_SIZE


dragon = pygame.sprite.Group()