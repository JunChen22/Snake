#simple snake game

from random import randint
import pygame
import sys
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    # while True:
    play()

def update():
    pygame.display.update()

# spawn a food for the snake
def food():
    pass

def control(dire, snakeLength, input):
    if snakeLength > 1:
        if (input == K_UP) and dire != 'DOWN': dire = 'UP'
        if (input == K_DOWN) and dire != 'UP': dire = 'DOWN'
        if (input == K_RIGHT) and dire != 'LEFT': dire = 'RIGHT'
        if (input == K_LEFT) and dire != 'RIGHT': dire = 'LEFT'
    elif snakeLength == 1:
        if (input == K_UP): dire = 'UP'
        if (input == K_DOWN): dire = 'DOWN'
        if (input == K_RIGHT): dire = 'RIGHT'
        if (input == K_LEFT): dire = 'LEFT'

    return dire

def display():
    pass

# snake body
def body():
    pass

# the loop of main control
def play():
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    tittle = pygame.display.set_caption('Snakey')
    snakeHead = pygame.image.load('image/snake.png')

    snakeX = randint(1,WIDTH-1)
    snakeY = randint(1,HEIGHT-1)

    current_dire = 'DOWN'
    snakeLength = 1

    while True:
        window.fill((255, 255, 255))
        window.blit(snakeHead, (snakeX, snakeY))
        # will fall out of this for loop if no key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when clicked on X (exit)
                quitgame()
            elif event.type == KEYDOWN:
                current_dire = control(current_dire, snakeLength, event.key)

        if current_dire == 'UP': snakeY -= 10
        if current_dire == 'DOWN': snakeY += 10
        if current_dire == 'RIGHT': snakeX += 10
        if current_dire == 'LEFT': snakeX -= 10
        pygame.display.update()
        clock.tick(12)

def quitgame():
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
