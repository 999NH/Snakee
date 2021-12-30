import pygame
import sys
import random



pygame.init()
color1 = (170, 215, 81)
color2 = (162, 209, 73)


class Snake:
    def __init__(self, länge):
        self.länge = länge
        self.Weg = []




    def increaseLänge(self):
        self.länge += 1


class Food:
    def __init__(self, x, y):
        self.exist = False
        self.x = x
        self.y = y

    def erscheinen(self):
        self.exist = True

    def verschwinden(self):
        self.exist = False

class Head:
    def __init__(self, speedx, speedy, position):
        self.speedx = speedx
        self.speedy = speedy
        self.position  = position



class Tile:
    def __init__(self, xKoordinate, yKoordinate, position):
        self.xKoordinate = xKoordinate
        self.yKoordinate = yKoordinate
        self.position = position

    def bewegen(self, xSchritt, ySchritt):
        self.Weg.append(self.position)
        xKoordinate += xSchritt
        yKoordinate += ySchritt



while True:
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 800))
    surface.fill(color1)

    #Grid
    #Gridlength = 40px
    y = 0
    x = 0
    while x <= 800:
        while y <= 800:
            pygame.draw.rect(surface, color2, (x, y, 40, 40))
            y += 80
        y = 0
        x += 80

    y = 40
    x = 40
    while x <= 800:
        while y <= 800:
            pygame.draw.rect(surface, color2, (x, y, 40, 40))
            y += 80
        y = 40
        x += 80


    pygame.display.set_caption("Sneik")
    pygame.display.flip()



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass
                    # später: Pause

                if event.key == pygame.K_DOWN:
                    pass

                if event.key == pygame.K_RIGHT:
                    pass

                if event.type == pygame.K_LEFT:
                    pass

                if event.type == pygame.K_UP:
                    pass



    clock.tick(60)

        #pygame.draw.rect(surface, Quadrat, (400, 400))

