import pygame
import time
import random
import settings


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x=800, y=100, speed = 2):
        super().__init__()
        self.right_image = pygame.image.load('assets/images/purple_fish.png').convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        self.speed = speed
        self.rect = pygame.rect.Rect(x,y,self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):

        if self.moving_left:
            self.rect.x -= self.speed
            self.image = self.left_image

        elif self.moving_right:
            self.rect.x += self.speed
            self.image = self.right_image
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 2

        if self.rect.right <= 0:
            self.rect.x = settings.SCREEN_WIDTH + random.randint( 2*settings.TILE_SIZE, 5*settings.TILE_SIZE)
            self.rect.y = random.randint(0, settings.SCREEN_HEIGHT)


