import pygame
import time
import settings
import random
import dragon
from enemy import *
from stardust import *
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
#draw Characters
my_dragon = dragon.Dragon()

for i in range(random.randint(5,8)):
    stardusts.add(Stardust(random.randint(0,settings.SCREEN_WIDTH),random.randint(0,settings.SCREEN_HEIGHT - 2*settings.TILE_SIZE)))

for i in range(random.randint(2,4)):
    small_enemies.add(Enemy((random.randint(settings.SCREEN_WIDTH- settings.TILE_SIZE, settings.SCREEN_WIDTH + 2*settings.TILE_SIZE)),
                            random.randint(0,settings.SCREEN_HEIGHT- settings.TILE_SIZE),random.randint(2,5)))

draw_backround()

killed = pygame.sprite.spritecollide(my_dragon,small_enemies, False)
score = 0
while my_dragon.rect.y != (settings.SCREEN_HEIGHT - settings.TILE_SIZE) and len(killed) == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Game ended')
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_dragon.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_dragon.moving_right = True
            if event.key == pygame.K_SPACE:
                my_dragon.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_dragon.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_dragon.moving_right = False
            if event.key == pygame.K_SPACE:
                my_dragon.moving_up = False

    my_dragon.update()
    small_enemies.update( )
    stardusts.update()

    killed = pygame.sprite.spritecollide(my_dragon,small_enemies, False)
    stardust_collected = pygame.sprite.spritecollide(my_dragon, stardusts, True)
    if len(stardusts) == 0:
        for i in range(random.randint(5, 10)):
            stardusts.add(Stardust((random.randint(settings.SCREEN_WIDTH + settings.TILE_SIZE,settings.SCREEN_WIDTH + 20*settings.TILE_SIZE)), random.randint(0, settings.SCREEN_HEIGHT - 2*settings.TILE_SIZE)))
    score += len(stardust_collected)
    print(score)

    screen.blit(background, (0, 0))
    small_enemies.draw(screen)
    stardusts.draw(screen)
    my_dragon.draw(screen)
    pygame.display.flip()
    clock.tick(60)