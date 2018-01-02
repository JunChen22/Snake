# simple snake game

from random import randint
import pygame
import sys
from pygame.locals import *
import time

WIDTH = 800
HEIGHT = 600
CELL = 10

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

cSec = 0
cFrame = 0
FPS = 0

snakeSpeed = 17

window = pygame.display.set_mode((WIDTH, HEIGHT))
tittle = pygame.display.set_caption('Snakey')

def main():
    # while True:
    play()

def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")


def update():
    pygame.display.update()


# spawn a food for the snake
# initial food cant spawn in snake first location
def newfood(snakeX, snakeY):
    foodX = randint(1, WIDTH)*CELL
    foodY = randint(1, HEIGHT)*CELL

    while foodX is snakeX and foodY is snakY:
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


def atefood(snakeCoord, foodCoord):
    pass

# the loop of main control
def play():
    pygame.init()
    clock = pygame.time.Clock()

    snakeX = randint(1, WIDTH - 1)
    snakeY = randint(1, HEIGHT - 1)

    snakeCoord = [{'X': snakeX, 'Y': snakeY}]

    foodCoord = newfood(snakeX, snakeY)
    fps_font = pygame.font.Font('freesansbold.ttf', 18)

    current_dire = 'NONE'
    snakeLength = 1
    snakeHead = 0

    while True:
        window.fill(BLACK)

        # will fall out of this for loop if no key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when clicked on X (exit)
                quitgame()
            elif event.type == KEYDOWN:
                current_dire = control(current_dire, snakeLength, event.key)

        # to show fps/game speed
        count_fps()
        fps_overlay = fps_font.render(str(FPS), True, YELLOW)
        window.blit(fps_overlay, (0, 0))


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

        if current_dire != 'NONE': snakeCoord.pop()

        # atefood(snakeCoord,foodCoord)
        displaysnake(snakeCoord)
        displayfood(foodCoord)


        pygame.display.update()
        clock.tick(snakeSpeed)

def quitgame():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
