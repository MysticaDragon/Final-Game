import pygame
import time
import random
import settings
import dragon
pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
background = screen.copy()
clock = pygame.time.Clock()
# cut scene 1 bg
town = pygame.image.load('assets/images/bg_town.png').convert()
town.set_colorkey((0, 0, 0))

# intro catch your dragon bg
forest = pygame.image.load('assets/images/bg_1.png').convert()
forest.set_colorkey((0, 0, 0))

# skies
c1 = pygame.image.load('assets/images/clouds_1.png').convert()
c1.set_colorkey((0, 0, 0))
c2 = pygame.image.load('assets/images/clouds_2.png').convert()
c2.set_colorkey((0, 0, 0))
c3 = pygame.image.load('assets/images/clouds_3.png').convert()
c3.set_colorkey((0, 0, 0))
c4 = pygame.image.load('assets/images/clouds_4.png').convert()
c4.set_colorkey((0, 0, 0))
c5 = pygame.image.load('assets/images/clouds_5.png').convert()
c5.set_colorkey((0, 0, 0))
c6 = pygame.image.load('assets/images/clouds_6.png').convert()
c6.set_colorkey((0, 0, 0))
c7 = pygame.image.load('assets/images/clouds_7.png').convert()
c7.set_colorkey((0, 0, 0))
c8 = pygame.image.load('assets/images/clouds_8.png').convert()
c8.set_colorkey((0, 0, 0))
clouds = [c1,c2,c3,c4,c5,c6,c7,c8]
cloud = random.randint(0,7)
def draw_backround():
    background.blit(clouds[cloud],(0,0),)
my_dragon = dragon.Dragon()

draw_backround()

while my_dragon.rect.y != (settings.SCREEN_HEIGHT - settings.TILE_SIZE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Game ended')
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_dragon.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_dragon.moving_right = True
            if event.key == pygame.K_UP:
                my_dragon.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_dragon.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_dragon.moving_right = False
            if event.key == pygame.K_UP:
                my_dragon.moving_up = False

    my_dragon.update()

    screen.blit(background, (0, 0))
    my_dragon.draw(screen)
    pygame.display.flip()
    clock.tick(60)