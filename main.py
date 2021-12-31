import pygame
import sys
from pygame.math import Vector2
import random


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_part = False

        #images


    def draw_snake(self):
        for part in self.body:
            x_pos = part.x * Gridsize
            y_pos = part.y * Gridsize
            body_rect = pygame.Rect(x_pos, y_pos, Gridsize, Gridsize)
            pygame.draw.rect(surface, 'blue', body_rect)

    def move_snake(self):
        if self.new_part == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_part = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_part(self):
        self.new_part = True


class Food:
    def __init__(self):
        self.respawn()

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * Gridsize, self.pos.y * Gridsize, Gridsize, Gridsize)
        surface.blit(apple, food_rect)
        #pygame.draw.rect(surface, 'red', food_rect)

    def respawn(self):
        self.x = random.randint(0, Gridnumber)
        self.y = random.randint(0, Gridnumber)
        self.pos = Vector2(self.x, self.y)  # Vektor


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]: #Food & Head of snake at same position
            self.food.respawn()
            self.snake.add_part()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= Gridnumber or not 0 <= self.snake.body[0].y <= Gridnumber:
            self.game_over()

        for part in self.snake.body[1:]:#All elements except for the head
            if part == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()
        sys.exit()




Gridnumber = 19
Gridsize = 40
def grid():#Grid, 19 tiles
    color1 = (170, 215, 81)
    color2 = (162, 209, 73)
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




pygame.init()

#settings
pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sneik")
#images
apple = pygame.image.load('assets/Graphics/apple.png').convert_alpha()


#main class
main_game = Main()

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
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction == Vector2(0,-1):
                    pass
                else:
                    main_game.snake.direction = Vector2(0,1)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction == Vector2(-1,0):
                    pass
                else:
                    main_game.snake.direction = Vector2(1,0)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction == Vector2(1,0):
                    pass
                else:
                    main_game.snake.direction = Vector2(-1,0)

            if event.key == pygame.K_UP:
                if main_game.snake.direction == Vector2(0,1):
                    pass
                else:
                    main_game.snake.direction = Vector2(0,-1)



    grid()
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)


