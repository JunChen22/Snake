###simple snake game
###then after finsih would like to
###add some difficulity like flip image or something of some
###sort of blocks that limites the player
###...

from random import randint
import pygame
import sys
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

DIR = {'UP',  'DOWN','RIGHT','LEFT'}

Reve_DIR = {'UP': ('UP','DOWN'),
            'DOWN': ('UP','DOWN'),
            'RIGHT': ('RIGHT','LEFT'),
            'LEFT':('RIGHT','LEFT')}

snakeX = 80
snakeY = 140
current_dire = None
snakeLength = 1

def main():

    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    tittle = pygame.display.set_caption("Snakey")
    snakeHead = pygame.image.load("image/snake.png")

    while True:
        play()


def update():
    pygame.display.update()

#spawn a food for the snake
def food():
    pass

#sets the snake control logic
### def continue_movement():
###       dir[current_dire]


### 1  notthing pressed , not going
### 2  pressed goes one direction and all direction with only head
### 3 pressed goes one direction and 2 direicont only
### 4  goes and only goes one direcion if not pressed
###
def control(input):

    if snakeLength > 1:
        movement(input)
    elif snakeLength == 1:
        if  current_dire == "UP":
            move_up()
        if  current_dire == "DOWN":
            move_down()
        if  current_dire == "RIGHT":
            move_left()
        if  current_dire == "LEFT":
            move_right()

#determining where to move
# no same direction or reverse direction
def movement(input):

    if input == K_UP and current_dire not in Reve_DIR:
        move_up()
    elif input == K_DOWN and current_dire not in Reve_DIR:
        move_down()
    elif input == K_RIGHT and current_dire not in Reve_DIR:
        move_right()
    elif input == K_LEFT and current_dire not in Reve_DIR:
        move_left()
    else:
        pass

def move_up():
    current_dire = "UP"
    snakeY-=1

def move_down():
    current_dire = "DOWN"
    snakeY+= 1

def move_right():
    current_dire = "RIGHT"
    snakeX+= 1

def move_left():
    current_dire = "LEFT"
    snakeX-= 1



def display():
    window.fill((255, 255, 255))
    window.blit(snakeHead, (snakeX,snakeY))

#snake body
def body():
    pass

#the loop of main control
def play():

    while True:
        display()
        #will fall out of this for loop if no key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                control(event.key)

            print("something")
        pygame.display.update()
        clock.tick(60)

#snaked died , new game
def newGame():
    pass

def quitgame():
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()


