# simple snake game

from random import randint
import pygame
import sys
from pygame.locals import *
import time


#use map to represent x and y coordinate is not bad. i like it



WIDTH = 800
HEIGHT = 600

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

YELLOW = (255,255,0)

cSec = 0
cFrame = 0
FPS = 0



def main():
    # while True:
    play()

def window(snakeX,snakeY):

    error_message()
    pygame.quit()

def error_message():
    pass

def show_fps():
    pass


def count_fps():
    global cSec,cFrame,FPS

    if cSec == time.strftime("%S"):
        cFrame+=1
    else:
        FPS = cFrame
        cFrame=0
        cSec= time.strftime("%S")

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

# snake body
def body():
    pass

def random_location():
    pass


# the loop of main control
def play():
    pygame.init()
    clock = pygame.time.Clock()
    snakeSpeed = 30
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    tittle = pygame.display.set_caption('Snakey')
    snakeHead = pygame.image.load('image/snake.png')
    fps_font = pygame.font.Font('freesansbold.ttf', 18)
    snakeX = randint(1, WIDTH - 1)
    snakeY = randint(1, HEIGHT - 1)


    current_dire = 'none'
    snakeLength = 1

    while True:
        window.fill((0, 0, 0))
        window.blit(snakeHead, (snakeX, snakeY))
        # will fall out of this for loop if no key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when clicked on X (exit)
                quitgame()
            elif event.type == KEYDOWN:
                current_dire = control(current_dire, snakeLength, event.key)

        #to show fps/game speed
        count_fps()
        fps_overlay = fps_font.render(str(FPS), True, YELLOW)
        window.blit(fps_overlay, (0, 0))

        if current_dire == 'UP': snakeY -= 10
        if current_dire == 'DOWN': snakeY += 10
        if current_dire == 'RIGHT': snakeX += 10
        if current_dire == 'LEFT': snakeX -= 10
        pygame.display.update()
        clock.tick(snakeSpeed)


def quitgame():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
