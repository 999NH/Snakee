import pygame
import sys
from pygame.math import Vector2
import random

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_part = False

        #images
        self.head_up = pygame.image.load('assets/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('assets/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('assets/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('assets/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('assets/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('assets/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('assets/Graphics/body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/Graphics/body_topleft.png').convert_alpha()
        self.body_br = pygame.image.load('assets/Graphics/body_bottomright.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/Graphics/body_bottomleft.png').convert_alpha()


    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, part in enumerate(self.body):
            x_pos = part.x * Gridsize
            y_pos = part.y * Gridsize
            body_rect = pygame.Rect(x_pos, y_pos, Gridsize, Gridsize)
            if index == 0:
                surface.blit(self.head, body_rect)
            elif index == len(self.body) - 1:
                surface.blit(self.tail, body_rect)
            else:
                previous_part = self.body[index + 1] - part
                next_part = self.body[index -1] - part
                if previous_part.x == next_part.x:
                    surface.blit(self.body_vertical, body_rect)
                elif previous_part.y == next_part.y:
                    surface.blit(self.body_horizontal, body_rect)
                else:
                    if previous_part.x == -1 and next_part.y == -1 or previous_part.y == -1 and next_part.x == -1:
                        surface.blit(self.body_tl, body_rect)
                    elif previous_part.x == -1 and next_part.y == 1 or previous_part.y == 1 and next_part.x == -1:
                        surface.blit(self.body_bl, body_rect)
                    elif previous_part.x == 1 and next_part.y == -1 or previous_part.y == -1 and next_part.x == 1:
                        surface.blit(self.body_tr, body_rect)
                    elif previous_part.x == 1 and next_part.y == 1 or previous_part.y == 1 and next_part.x == 1:
                        surface.blit(self.body_br, body_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.head_left
        elif head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(0,1):
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

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

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


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
        self.grid()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]: #Food & Head of snake at same position
            self.food.respawn()
            self.snake.add_part()

        for part in self.snake.body[1:]:#Food doesn't spawn in snake
            if part == self.food.pos:
                self.food.respawn()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= Gridnumber or not 0 <= self.snake.body[0].y <= Gridnumber:
            self.game_over()

        for part in self.snake.body[1:]:#All elements except for the head
            if part == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        self.snake.reset()

    def grid(self):
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

    def pause(self):
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

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, 'black')
        score_x = int(Gridsize * Gridnumber - 60)
        score_y = int(Gridsize * Gridnumber - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

        surface.blit(score_surface, score_rect)
        surface.blit(apple, apple_rect)





Gridnumber = 19
Gridsize = 40

#settings
pygame.init()
game_font = pygame.font.Font('Font/poetsen_one/PoetsenOne-Regular.ttf', 25)
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
                main_game.pause()

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



    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)


