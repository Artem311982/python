import random

import pygame
from pygame.constants import QUIT

pygame.init()

FPS = pygame.time.Clock()

height = 800
width = 1200

color_white = (255, 255, 255)
color_black = (0, 0, 0)

main_display = pygame.display.set_mode((width, height))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(color_white)
player_rect = player.get_rect()
# player_speed = [1, 1]

playing = True

while playing:
    FPS.tick(500)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(color_black)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN]:
        print("Pressed")

    # if player_rect.bottom >= height:
    #     player_speed = random.choice(([1, -1], [-1, -1]))

    # if player_rect.top < 0:
    #     player_speed = random.choice(([-1, 1], [1, 1]))

    # if player_rect.right >= width:
    #     player_speed = random.choice(([-1, -1], [11, 1]))

    # if player_rect.left < 0:
    #     player_speed = random.choice(([1, 1], [1, -1]))

    # if player_rect.bottom >= height:
    #     player_speed[1] = -player_speed[1]

    # if player_rect.right >= width:
    #     player_speed[0] = -player_speed[0]

    # if player_rect.top < 0:
    #     player_speed[1] = -player_speed[1]

    # if player_rect.left < 0:
    #     player_speed[0] = -player_speed[0]

    main_display.blit(player, player_rect)

    # player_rect = player_rect.move(player_speed)

    pygame.display.flip()
