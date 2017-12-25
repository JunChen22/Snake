###simple snake game
###then after finsih would like to
###add some difficulity like flip image or something of some
###sort of blocks that limites the player
###...

from random import randint
import pygame

WIDTH = 800
HEIGHT = 600

class Snake():

    randomX = randint(1, WIDTH-1)
    randomY = randint(1, HEIGHT-1)
    current_dire = None
    snakeX = 80
    snakeY = 140
    snakeLength = 1

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.crashed = False
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

        dir = ["up","down","right","left"]

    #determine whats being pressed in hte the main part
    if snakeLength >1:
        if input == 273:
            print("pressed up")
            if self.current_dire != (dir[0] and dir[1]):
                self.current_dire ="up"
                self.snakeY-=10
        elif input == 274:
            print("pressed down")
            if self.current_dire != (dir[0] and dir[1]):
                self.current_dire ="down"
                self.snakeY+=10
        elif input == 275:
            print("pressed right")
            if self.current_dire != (dir[2] and dir[3]):
                self.current_dire ="right"
                self.snakeX+=10
        elif input == 276:
            print("pressed left")
            if self.current_dire != (dir[2] and dir[3]):
                self.current_dire ="left"
                self.snakeX-=10
        else:
            pass

    else:
        print("length is still one ")


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
    game.quitgame()


