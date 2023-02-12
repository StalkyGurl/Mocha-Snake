'''
This is the main driver file.
'''

import pygame as p
from os import path
from time import sleep
from snake import *
from coffee import *

SNAKE_SPEED = 9
FPS = 60
WIDTH = HEIGHT = 700
SCORE_SPACE = 50
DIMENSION = 20
SQ_SIZE = WIDTH // DIMENSION
screen = p.display.set_mode((WIDTH, HEIGHT + SCORE_SPACE))
icon = p.image.load("images/icon.png")
p.display.set_icon(icon)
p.display.set_caption('Mocha Snake')
clock = p.time.Clock()
bg = p.image.load("images/game_bg.png")
bg = p.transform.scale(bg, (WIDTH, HEIGHT))
p.mixer.init()
p.mixer.music.load("assets/bg_music.mp3")
p.mixer.music.play(-1, 0.0)
p.mixer.music.set_volume(0.05)
BEST_SCORE = 0


def get_font(size):
    return p.font.Font("assets/font.ttf", size)


def printScore(score):
    p.font.init()
    font = get_font(55)
    text = font.render(f'Score: ', True, '#7295CD')
    screen.blit(text, (10,690))
    font2 = p.font.SysFont('Verdana', 46)
    font2.set_bold(True)
    text2 = font2.render(f'{score}', True, '#7295CD')
    screen.blit(text2, (225, 695))


def printEndGameText(score):
    global BEST_SCORE
    p.font.init()
    font = get_font(55)
    text1 = font.render('Game Over!', True, '#1AB1E5')
    shadow1 = font.render('Game Over!', True, '#0D5660')
    text2 = font.render(f'Score: {score}', True, '#1AB1E5')
    shadow2 = font.render(f'Score: {score}', True, '#0D5660')
    text3 = font.render(f'Best Score: {BEST_SCORE}', True, '#1AB1E5')
    shadow3 = font.render(f'Best Score: {BEST_SCORE}', True, '#0D5660')
    text4 = font.render('New best score!', True, '#1AB1E5')
    shadow4 = font.render('New best score!', True, '#0D5660')

    font2 = get_font(30)
    shadow5 = font2.render("Press 'r' to restart the game", True, '#0D5660')
    text5 = font2.render("Press 'r' to restart the game", True, '#1693BE')
    screen.blit(shadow5, (WIDTH/2 - text5.get_width()/2 + 2, HEIGHT//2 + 355 + 2))
    screen.blit(text5, (WIDTH/2 - text5.get_width()/2, HEIGHT//2 + 355))

    screen.blit(shadow1, (WIDTH/2 - text1.get_width()/2 + 2, HEIGHT//2 - 100 + 2))
    screen.blit(shadow2, (WIDTH/2 - text2.get_width()/2 + 2, HEIGHT//2 - 50 + 2))
    screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT//2 - 100))
    screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT//2 - 50))
    if score != BEST_SCORE:
        screen.blit(shadow3, (WIDTH/2 - text3.get_width()/2 + 2, HEIGHT//2 + 2))
        screen.blit(text3, (WIDTH/2 - text3.get_width()/2, HEIGHT//2))
    else:
        screen.blit(shadow4, (WIDTH/2 - text4.get_width()/2 + 2, HEIGHT//2 + 2))
        screen.blit(text4, (WIDTH/2 - text4.get_width()/2, HEIGHT//2))


def main():
    p.init()
    pick = p.mixer.Sound(path.join('assets', 'pick.wav'))
    snake = Snake()
    running = True
    coffee = spawnCoffee(snake.coordinates)
    eaten = False
    end_game = False
    while running:
        screen.fill('black')
        screen.blit(bg, (0, 0))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.KEYDOWN and not end_game:
                if e.key == p.K_w and snake.direction != 'down':
                    snake.direction = 'up'
                elif e.key ==p.K_s and snake.direction != 'up':
                    snake.direction = 'down'
                elif e.key ==p.K_a and snake.direction != 'right':
                    snake.direction = 'left'
                elif e.key ==p.K_d and snake.direction != 'left':
                    snake.direction = 'right'
        if not end_game:
            if snake.coordinates[0] == (coffee.x, coffee.y):
                eaten = True
                snake.length += 1
                del coffee
                coffee = spawnCoffee(snake.coordinates)
                pick.play()

            printScore(snake.length)
            coffee.drawCoffee(screen)
            snake.moveSnake(eaten)
            snake.drawSnake(screen)
            eaten = False
            p.display.flip()
            sleep(SNAKE_SPEED/100)
            clock.tick(60)

        if snake.endGame():
            global BEST_SCORE
            end_game = True
            score = snake.length
            if score > BEST_SCORE:
                BEST_SCORE = score
            printEndGameText(score)
            p.display.flip()
            clock.tick(60)
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.KEYDOWN and e.key == p.K_r:
                    del snake
                    del coffee
                    snake = Snake()
                    coffee = spawnCoffee(snake.coordinates)
                    end_game = False
                    


if __name__  == '__main__':
    main()