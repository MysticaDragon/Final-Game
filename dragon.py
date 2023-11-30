import pygame
import random
import time
import settings


class Dragon(pygame.sprite.Sprite):
    def __init__(self, x=200, y=200):
        super().__init__()

        self.right_images = [pygame.image.load('assets/images/hero_1.png').convert(),
                             pygame.image.load('assets/images/hero_2.png').convert()]
        for img in self.right_images:
            img.set_colorkey((0, 0, 0))
        self.left_images = []
        for img in self.right_images:
            self.left_images.append(pygame.transform.flip(img, True, False))

        self.image_index = 0
        self.image = self.right_images[self.image_index]
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.use_right_images = True
        # self.right_image = pygame.image.load('assets/images/hero_1.png').convert()
        # self.right_image.set_colorkey((0, 0, 0))
        # self.left_image = pygame.transform.flip(self.right_image, True, False)
        # self.image = self.right_image
        # self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = True

        self.animation_delay = 100  # Delay between animation frames in milliseconds
        self.last_update = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def reset_position(self):
        self.x = 200
        self.y = 200

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.image_index = (self.image_index + 1) % len(self.right_images)

        if self.moving_left:
            self.rect.x -= 2
            self.image = self.left_images[self.image_index]
            self.use_right_images = False
        elif self.moving_right:
            self.rect.x += 2
            self.use_right_images = True
            self.image = self.right_images[self.image_index]
        if self.moving_up:
            self.rect.y -= 2
            if self.use_right_images:
                self.image = self.right_images[self.image_index]
            else:
                self.image = self.left_images[self.image_index]
        elif self.moving_down:
            self.rect.y += 4

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x >= settings.SCREEN_WIDTH - 2 * settings.TILE_SIZE:
            self.rect.x = settings.SCREEN_WIDTH - 2 * settings.TILE_SIZE
        if self.rect.y >= settings.SCREEN_HEIGHT - settings.TILE_SIZE:
            self.rect.y = settings.SCREEN_HEIGHT - settings.TILE_SIZE


dragon = pygame.sprite.Group()
