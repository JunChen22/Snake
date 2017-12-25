###simple snake game
###then after finsih would like to
###add some difficulity like flip image or something of some
###sort of blocks that limites the player
###...

from random import randint
import pygame
from msvcrt import kbhit


WIDTH = 800
HEIGHT = 600
DIR = {273: 'UP', 274: 'DOWN', 275:'RIGHT', 276: 'LEFT'}


class Snake():

    snakeX = 80
    snakeY = 140
    current_dire = None
    snakeLength = 1

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.tittle = pygame.display.set_caption("Snakey")
        self.snakeHead = pygame.image.load("image/snake.png")


    def update():
        pygame.display.update()

    #spawn a food for the snake
    def food():
        pass

    #sets the snake control logic
    def control(self,input):

        if input not in dir:
            pass
        elif self.snakeLength >1:
            self.movement(self.dir[input])
        else :#goes wheere ever wanted
            if  self.current_dire == "UP":
                self.snakeY -= 10
            if  self.current_dire == "DOWN":
                self.snakeY += 10
            if  self.current_dire == "RIGHT":
                self.snakeX += 10
            if  self.current_dire == "LEFT":
                self.snakeX -= 10
            else:


   ### def continue_movement(self):
 ###       dir[self.current_dire]
###
    ###   ### 1  notthing pressed , not going
 ###   2  pressed goes one direction and all direction with only head
   ###  3 pressed goes one direction and 2 direicont only
    ### 4  goes and only goes one direcion if not pressed
###

    def movement(self,input):

        if input == "UP":
            if self.current_dire != (dir[0] and dir[1]):
                self.current_dire = "UP"
        if input == "DOWN":
            if self.current_dire != (dir[0] and dir[1]):
                self.current_dire = "DOWN"
        if input == "RIGHT":
            if self.current_dire != (dir[2] and dir[3]):
                self.current_dire = "RIGHT"
        if input == "LEFT:
            if self.current_dire != (dir[2] and dir[3]):
                self.current_dire = "LEFT"

    def display(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.snakeHead, (self.snakeX,self.snakeY))

    #snake body
    def body():
        pass

    #the loop of main control
    def play(self):

        while True:
            self.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitgame()

                if event.type == pygame.KEYDOWN:
                    key = event.key
                    self.control(key)
                elif not kbhit():
                    self.control(self.current_dire)

                print("something")
            pygame.display.update()
            self.clock.tick(60)

    #snaked died , new game
    def newGame(self):
        pass

    def quitgame():
        pygame.quit()
        quit()


if __name__ == "__main__":

    game = Snake()
    game.play()


