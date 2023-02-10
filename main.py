'''
This is the main driver file.
'''

import pygame as p

FPS = 60
WIDTH = HEIGHT = 700
screen = p.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()
bg = p.image.load("images/game_bg.png")


def main():
    p.init()
    screen.fill('black')
    running = True
    while running:
        screen.blit(bg, (0, 0))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        p.display.flip()
        clock.tick(60)


if __name__  == '__main__':
    main()