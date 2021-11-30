import pygame
import sys
import random



pygame.init()



class Snake:
    def __init__(self, länge):
        self.länge = länge
        self.Weg = []



    def increaseLänge(self):
        self.länge += 1


class Essen:
    def __init__(self):
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
    surface.fill((110, 110, 5))
    pygame.display.set_caption("Sneik")
    background = pygame.image.load('assets/green-tree-python-1014229_1920.jpg')
    surface.blit(background, (-400, 0))
    pygame.display.flip()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if event.type == pygame.K_DOWN:
                pass

            if event.type == pygame.K_RIGHT:
                pass

            if event.type == pygame.K_LEFT:
                pass

            if event.type == pygame.K_UP:
                pass

        pygame.draw.rect(surface, Quadrat, (400, 400))

