# simple snake game

from random import randint
import pygame
import sys
from pygame.locals import *
import time

WIDTH = 800
HEIGHT = 600
CELL = 20

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
tittle = pygame.display.set_caption('Snakey')
snakeHead = 0


def wall(snakeCoord):
    if snakeCoord[snakeHead]['X'] == WIDTH or snakeCoord[snakeHead][
        'Y'] == HEIGHT or \
            snakeCoord[snakeHead]['X'] == 0 or snakeCoord[snakeHead]['Y'] == 0:
        quitgame()


def body(snakeCoord):
    if (len(snakeCoord) > 1):
        for snakeBody in snakeCoord[1:]:
            if snakeCoord[snakeHead] == snakeBody:
                quitgame()


# spawn a food for the snake
# initial food cant spawn in snake first location
def newfood(snakeCoord):
    foodX = randint(1, WIDTH)
    foodY = randint(1, HEIGHT)

    while foodX != snakeCoord[0]['X'] and foodY != snakeCoord[0][
        'Y'] or foodX % 10 != 0 or foodY % 10 != 0:
        foodX = randint(1, WIDTH)
        foodY = randint(1, HEIGHT)

    return {'X': foodX, 'Y': foodY}


def control(dire, snakeLength, input):
    if snakeLength > 1:
        if (input == K_UP) and dire != DOWN: dire = UP
        if (input == K_DOWN) and dire != UP: dire = DOWN
        if (input == K_RIGHT) and dire != LEFT: dire = RIGHT
        if (input == K_LEFT) and dire != RIGHT: dire = LEFT
    elif snakeLength == 1:
        if (input == K_UP): dire = UP
        if (input == K_DOWN): dire = DOWN
        if (input == K_RIGHT): dire = RIGHT
        if (input == K_LEFT): dire = LEFT

    return dire


# snake body
def displaysnake(snakeCoord):
    for length in snakeCoord:
        snake = pygame.Rect(length['X'], length['Y'], CELL, CELL)
        pygame.draw.rect(window, WHITE, snake)


def displayfood(foodCoord):
    food = pygame.Rect(foodCoord['X'], foodCoord['Y'], CELL, CELL)
    pygame.draw.rect(window, YELLOW, food)


# the loop of main control
def play():
    pygame.init()
    clock = pygame.time.Clock()

    snakeX = randint(1, WIDTH - 1)
    snakeY = randint(1, HEIGHT - 1)

    while snakeX % 10 != 0 or snakeY % 10 != 0:
        snakeX = randint(1, WIDTH - 1)
        snakeY = randint(1, HEIGHT - 1)

    snakeCoord = [{'X': snakeX, 'Y': snakeY}]

    foodCoord = newfood(snakeCoord)

    current_dire = 'NONE'
    snakeLength = 1

    tailes = 0
    snakeSpeed = 17
    while True:
        window.fill(BLACK)

        # will fall out of this for loop if no key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when clicked on X (exit)
                quitgame()
            elif event.type == KEYDOWN:
                current_dire = control(current_dire, snakeLength, event.key)

        if current_dire == 'UP':
            snakeCoord.insert(snakeHead, {'X': snakeCoord[snakeHead]['X'],
                                          'Y': snakeCoord[snakeHead]['Y'] - 10})
        if current_dire == 'DOWN':
            snakeCoord.insert(snakeHead, {'X': snakeCoord[snakeHead]['X'],
                                          'Y': snakeCoord[snakeHead]['Y'] + 10})
        if current_dire == 'RIGHT':
            snakeCoord.insert(snakeHead, {'X': snakeCoord[snakeHead]['X'] + 10,
                                          'Y': snakeCoord[snakeHead]['Y']})
        if current_dire == 'LEFT':
            snakeCoord.insert(snakeHead, {'X': snakeCoord[snakeHead]['X'] - 10,
                                          'Y': snakeCoord[snakeHead]['Y']})

        # NONE means no direction/keypressed doesnt start
        # if snake ate food , tail doesnt get pop
        # so it will "increase"
        if current_dire != 'NONE':

            # create newfood and tails but doenst actually do anything
            if snakeCoord[snakeHead]['X'] == foodCoord['X'] and \
                    snakeCoord[snakeHead]['Y'] == foodCoord['Y']:
                snakeLength += 2
                tailes += 1
                foodCoord = newfood(snakeCoord)
                snakeSpeed += 2
            # doesnt actually do anything but to avoid being being popped
            #  making the tail grows
            elif tailes > 0:
                tailes -= 1
            else:
                snakeCoord.pop()

        body(snakeCoord)
        wall(snakeCoord)

        displaysnake(snakeCoord)
        displayfood(foodCoord)

        pygame.display.update()
        clock.tick(snakeSpeed)


def quitgame():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    play()
