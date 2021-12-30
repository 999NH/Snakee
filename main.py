import pygame
import sys
from pygame.math import Vector2
import random



pygame.init()
color1 = (170, 215, 81)
color2 = (162, 209, 73)


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.Weg = []
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for part in self.body:
            x_pos = part.x * Gridsize
            y_pos = part.y * Gridsize
            body_rect = pygame.Rect(x_pos, y_pos, Gridsize, Gridsize)
            pygame.draw.rect(surface, 'blue', body_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]





    def increaseLänge(self):
        self.länge += 1


class Food:
    def __init__(self):
        self.x = random.randint(0, Gridnumber)
        self.y = random.randint(0, Gridnumber)
        self.pos = Vector2(self.x, self.y) #Vektor

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * Gridsize, self.pos.y * Gridsize, Gridsize, Gridsize)
        pygame.draw.rect(surface, 'red', food_rect)





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




#settings
pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sneik")

Gridnumber = 19
Gridsize = 40
def grid():#Grid, 19 tiles
    surface.fill(color1)
    gridy = 0
    gridx = 0
    while gridx <= 800:
        while gridy <= 800:
            pygame.draw.rect(surface, color2, (gridx, gridy, Gridsize, Gridsize))
            gridy += 80
        gridy = 0
        gridx += 80

    gridy = Gridsize
    gridx = Gridsize
    while gridx <= 800:
        while gridy <= 800:
            pygame.draw.rect(surface, color2, (gridx, gridy, Gridsize, Gridsize))
            gridy += 80
        gridy = Gridsize
        gridx += 80


# TestObjekt
test_essen = Food()
test_snake = Snake()

#Movement -> 150ms
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

#pause
def pause():
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
        pygame.display.update()
        clock.tick(60)

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            test_snake.move_snake()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()

            if event.key == pygame.K_DOWN:
                pass

            if event.key == pygame.K_RIGHT:
                pass

            if event.type == pygame.K_LEFT:
                pass

            if event.type == pygame.K_UP:
                pass


    grid()
    test_essen.draw_food()
    test_snake.draw_snake()

    pygame.display.update()
    clock.tick(60)

        #pygame.draw.rect(surface, Quadrat, (400, 400))

