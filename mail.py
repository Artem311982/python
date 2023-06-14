import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

color_white = (255, 255, 255)
color_black = (0, 0, 0)
colore_blue = (0, 0, 255)
color_green = (0, 255, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(color_white)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_up = [-1, 0]
player_move_left = [0, -1]


def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(colore_blue)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_rect)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

bonuses = []
enemies = []

playing = True

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

while playing:
    FPS.tick(500)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        # if event.type == CREATE_BONUS:
        #     bonuses.append(create_bonus())

    main_display.fill(color_black)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_move_right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move[enemy[2]]
        main_display.blit(enemy[0], enemy[1])
        
    for bonus in bonuses:
        bonus[1] = bonus[1].move[bonus[2]]
        main_display.blit(bonus[0], bonus[1])

    # enemy_rect = enemy_rect.move(enemy_move)

    main_display.blit(player, player_rect)

    # main_display.blit(enemy, enemy_rect)

    main_display(bonus, player_rect)

    print(len(enemies))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom < 0:
            bonuses.pop(bonuses.index(enemy))