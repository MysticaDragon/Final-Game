import pygame
import time
import settings
import random
import dragon
from score import *
from enemy import *
from stardust import *
from enemy_2 import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Children of the Stars')
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
background = screen.copy()
clock = pygame.time.Clock()

#Sounds
start_background_music = pygame.mixer.Sound('assets/sounds/start_screen_music.wav')
game_background_music = pygame.mixer.Sound('assets/sounds/play_screen_music.wav')
middle_backround_music = pygame.mixer.Sound('assets/sounds/waiting_music.wav')
button_sound = pygame.mixer.Sound('assets/sounds/bu.mp3')
death_sound = pygame.mixer.Sound('assets/sounds/death_sound.wav')
stardust_collection_sound = pygame.mixer.Sound('assets/sounds/stardust_sound.wav')
#channels
pygame.mixer.set_num_channels(5)  # Adjust the number based on your needs
bg_music_channel = pygame.mixer.Channel(0)
button_channel = pygame.mixer.Channel(1)
stardust_channel = pygame.mixer.Channel(2)
wait_channel = pygame.mixer.Channel(3)
death_channel = pygame.mixer.Channel(4)

# Backgrounds
# start
start_screen = pygame.image.load('assets/images/start_screen.PNG').convert()
start_screen.set_colorkey((0, 0, 0))
# instructions
instructions_bg = pygame.image.load('assets/images/instructions_1.PNG').convert()
instructions_bg.set_colorkey((0, 0, 0))
# end screen
end_screen_bg = pygame.image.load('assets/images/end_screen.PNG').convert()
end_screen_bg.set_colorkey((0, 0, 0))

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
clouds = [c1, c2, c3, c4, c5, c6, c7, c8]
cloud = random.randint(0, 7)

# score counter
my_score = Score()


def draw_start_background():
    background.blit(start_screen, (0, 0), )


def draw_instructions_background():
    background.blit(instructions_bg, (0, 0), )


def draw_end_background():
    background.blit(end_screen_bg, (0, 0))


def draw_cloud_background():
    cloud = random.randint(0, 7)
    background.blit(clouds[cloud], (0, 0), )


def draw_score():
    background.blit(my_score.image, (my_score.x, my_score.y))
    background.blit(my_score.score_msg,
                    (settings.SCREEN_WIDTH - 1.95 * settings.TILE_SIZE, settings.TILE_SIZE / 3))

def play_intro_music():
    start_background_music.set_volume(0.6)
    bg_music_channel.play(start_background_music, loops=-1)

def play_wait_music():
    middle_backround_music.set_volume(0.6)
    wait_channel.play(middle_backround_music, loops=-1)
def play_button():
    button_sound.set_volume(1)
    button_channel.play(button_sound)
    pygame.display.flip()
    pygame.time.delay(400)

def play_stardust():
    stardust_collection_sound.set_volume(1)
    stardust_channel.play(stardust_collection_sound)
    pygame.display.flip()

def play_death():
    death_sound.set_volume(1)
    death_channel.play(death_sound)
    pygame.display.flip()
    pygame.time.delay(400)

def play_game_music():
    game_background_music.set_volume(0.4)
    bg_music_channel.play(game_background_music, loops=-1)

def stop_intro_music():
    pygame.mixer.Sound.stop(start_background_music)

def stop_game_music():
    pygame.mixer.Sound.stop(game_background_music)

def stop_wait_music():
    pygame.mixer.Sound.stop(middle_backround_music)
    pygame.mixer.Channel(3).stop()
def init_characters():
    global my_dragon
    # draw main character
    my_dragon = dragon.Dragon()
    # generating initial stardust
    for i in range(random.randint(5, 8)):
        stardusts.add(Stardust(random.randint(settings.SCREEN_WIDTH - 7 * settings.TILE_SIZE,
                                              settings.SCREEN_WIDTH + 4 * settings.TILE_SIZE),
                               random.randint(0, settings.SCREEN_HEIGHT - 2 * settings.TILE_SIZE)))
    # made small enemies
    for i in range(random.randint(2, 4)):
        small_enemies.add(Enemy(
            (random.randint(settings.SCREEN_WIDTH + settings.TILE_SIZE,
                            settings.SCREEN_WIDTH + 6 * settings.TILE_SIZE)),
            random.randint(0, settings.SCREEN_HEIGHT - 3*settings.TILE_SIZE), random.randint(2, 4)))
    #large enemies
    for i in range(random.randint(2, 3)):
        large_enemies.add(BigEnemy(
            (random.randint(settings.SCREEN_WIDTH + 12 * settings.TILE_SIZE,
                            settings.SCREEN_WIDTH + 20 * settings.TILE_SIZE)),
            random.randint(0, settings.SCREEN_HEIGHT ), random.randint(1, 2)))


def instructions():
    play_wait_music()
    while True:
        draw_instructions_background()
        # tracking mouse
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Game ended')
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 351 < mouse_pos[0] <= 480 and 413 < mouse_pos[1] <= 481:
                    play_button()
                    return 'play'
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    stop_wait_music()
    return 'play'


def play():
    reset_game()
    play_game_music()
    init_characters()
    draw_cloud_background()
    killed = pygame.sprite.spritecollide(my_dragon, small_enemies, False)
    killed2 = pygame.sprite.spritecollide(my_dragon, large_enemies, False)
    while my_dragon.rect.y != (settings.SCREEN_HEIGHT - settings.TILE_SIZE) and len(killed) == 0 and len(killed2) == 0:
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
        large_enemies.update()
        small_enemies.update()
        stardusts.update()
        killed = pygame.sprite.spritecollide(my_dragon, small_enemies, False)
        killed2 = pygame.sprite.spritecollide(my_dragon, large_enemies, False)
        stardust_collected = pygame.sprite.spritecollide(my_dragon, stardusts, True)
        count = 0
        if len(stardust_collected) > count:
            count += 1
            my_score.update()
            my_score.update_score_text()
            play_stardust()
        draw_score()
        if len(stardusts) == 0:
            for i in range(random.randint(5, 10)):
                stardusts.add(Stardust((random.randint(settings.SCREEN_WIDTH + settings.TILE_SIZE,
                                                       settings.SCREEN_WIDTH + 20 * settings.TILE_SIZE)),
                                       random.randint(0, settings.SCREEN_HEIGHT - 2 * settings.TILE_SIZE)))
        if 10 <= my_score.print_score() < 11:
            print('big enemy')
            for enemy in large_enemies:
                enemy.start()
        my_score.update_high_score()
        my_score.update_highscore_text()
        screen.blit(background, (0, 0))
        # my_score.draw(screen)
        small_enemies.draw(screen)
        large_enemies.draw(screen)
        stardusts.draw(screen)
        my_dragon.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    play_death()
    stop_game_music()
    return 'end'


def reset_game():
    for enemy in small_enemies:
        enemy.kill()
    for enemy in large_enemies:
        enemy.kill()
    for stardust in stardusts:
        stardust.kill()
    my_score.reset()


def start():
    play_intro_music()
    while True:
        # start screen
        draw_start_background()
        # tracking mouse
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Game ended')
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 633 < mouse_pos[0] <= 814 and 383 < mouse_pos[1] <= 441:
                    play_button()
                    print('you can start')
                    stop_intro_music()
                    return 'intro'
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def end_screen():
    play_wait_music()
    while True:
        # start screen
        draw_end_background()
        # tracking mouse
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Game ended')
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 216 < mouse_pos[0] <= 675 and 298 < mouse_pos[1] <= 369:
                    play_button()
                    stop_wait_music()
                    play()

        background.blit(my_score.score_msg,
                        (405, 165))
        background.blit(my_score.highscore_msg,
                        (405, 248))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)


while True:
    state = start()
    if state == 'quit':
        break
    elif state == 'intro':
        instructions()
        play()
        end_screen()
