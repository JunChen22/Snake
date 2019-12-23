import pygame
# componet of Pong
# 1.the ball
# 2.the paddle(user vs cpu)

# the ball
#-starts in the middle of the screen
#-winner serve , starts off by cpu

WIDTH = 800
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
tittle = pygame.display.set_caption('Pong')


def ball():
    pass

# ball movement
#-speed
#-direction vs paddle position
#-hit wall will change direction but maintain the angle
#-generate it when it reach the end(left/right wall)
#-goes to winner , starts from going to player when input detected

# user control
# using up/down button for control

# game pace
# gets faster and faster

# cpu
# enemy moves faster as users gets more point
# speed will determin the ability to reach for the ball


# game size
# 800 x 600
#black and white
# paddle size TBT

def play():

    pygame.init()
    while True:
        pygame.display.update()

    pass


def quitgame():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    play()
