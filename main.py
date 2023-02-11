'''
This is the main driver file.
'''

import pygame as p
from time import sleep
from snake import *
from coffee import *

SNAKE_SPEED = 6
FPS = 60
WIDTH = HEIGHT = 700
DIMENSION = 20
SQ_SIZE = WIDTH // DIMENSION
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Mocha Snake')
clock = p.time.Clock()
bg = p.image.load("images/game_bg.png")


def main():
    p.init()
    screen.fill('black')
    snake = Snake()
    running = True
    coffee = spawnCoffee(snake.coordinates)
    eaten = False
    while running:
        screen.blit(bg, (0, 0))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_w and snake.direction != 'down':
                    snake.direction = 'up'
                elif e.key ==p.K_s and snake.direction != 'up':
                    snake.direction = 'down'
                elif e.key ==p.K_a and snake.direction != 'right':
                    snake.direction = 'left'
                elif e.key ==p.K_d and snake.direction != 'left':
                    snake.direction = 'right'

        if snake.coordinates[0] == (coffee.x, coffee.y):
            eaten = True
            snake.length += 1
            del coffee
            coffee = spawnCoffee(snake.coordinates)

        if snake.endGame():
            sleep(5)
            running = False



        coffee.drawCoffee(screen)
        snake.moveSnake(eaten)
        snake.drawSnake(screen)
        eaten = False
        p.display.flip()
        sleep(SNAKE_SPEED/100)
        clock.tick(60)


if __name__  == '__main__':
    main()