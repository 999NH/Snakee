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


class Essen:
    def __init__(self, xKoordinate, yKoordinate):
        self.exist = False
        self.xKoordinate = xKoordinate
        self.yKoordinate = yKoordinate

    def erscheinen(self):
        self.exist = True

    def verschwinden(self):
        self.exist = False


class Quadrat:
    def __init__(self, xKoordinate, yKoordinate):
        self.xKoordinate = xKoordinate
        self.yKoordinate = yKoordinate

    def bewegen(self, xSchritt, ySchritt):
        xKoordinate += xSchritt
        yKoordinate += ySchritt



if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((800, 800))
    surface.fill(color1)
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

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_DOWN:
                    #später: Pause
                    pass

                if event.key == pygame.K_RIGHT:
                    pass

                if event.type == pygame.K_LEFT:
                    pass

                if event.type == pygame.K_UP:
                    pass

            if event.type == pygame.QUIT:
                running = False




        #pygame.draw.rect(surface, Quadrat, (400, 400))

