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
        window = pygame.display.set_mode((800, 600))
        tittle = pygame.display.set_caption("Snakey")

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
    ###  firstSnakeGame = Snake(2,3)
    gameDisplay = pygame.display.set_mode((800,600))

    clock = pygame.time.Clock()
    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)

        pygame.display.update()
        clock.tick(60)



    pygame.quit()
    quit()


###simple snake game
###then after finsih would like to
###add some difficulity like flip image or something of some
###sort of blocks that limites the player
###...