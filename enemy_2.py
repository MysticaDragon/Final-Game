import pygame
import time
import random
import settings


class BigEnemy(pygame.sprite.Sprite):
    def __init__(self, x=800, y=100, speed = 2):
        super().__init__()
        self.right_images = [pygame.image.load('assets/images/large_enemy_1.png').convert(),
                             pygame.image.load('assets/images/large_enemy_2.png').convert()]
        for img in self.right_images:
            img.set_colorkey((0, 0, 255))
        self.left_images = []
        for img in self.right_images:
            self.left_images.append(pygame.transform.flip(img, True, False))

        self.image_index = 0
        self.image = self.right_images[self.image_index]
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.speed = speed
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.animation_delay = 400  # Delay between animation frames in milliseconds
        self.last_update = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.image_index = (self.image_index + 1) % len(self.right_images)

        if self.moving_left:
            self.rect.x -= self.speed
            self.image = self.left_images[self.image_index]

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

    def reset(self):
        self.kill()


large_enemies = pygame.sprite.Group()