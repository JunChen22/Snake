from msvcrt import kbhit
from random import randint
from time import clock
from time import sleep
import pygame

WIDTH = 800
HEIGHT = 600

class Snake():

    randomX = randint(1, WIDTH-1)
    randomY = randint(1, HEIGHT-1)

    def __init__(self, snakeX,snakeY):

        pygame.init()
        gameDisplay = pygame.display.set_mode((800, 600))

    def update():
        pygame.display.update()
        pass

    def food():
        pass

    def controlLogic():
        pass

    def kbinput():
        pass

    def display():
        pass

    def body():
        pass

    def quitgame():
        pygame.quit()
        quit()


if __name__ == "__main__":
    pass
