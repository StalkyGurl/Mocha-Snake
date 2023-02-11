'''
This file contains Coffee class.
'''

import pygame as p
from random import randint, choice

SQ_SIZE = 35

coffee = p.image.load("images/coffee.png")
coffee = p.transform.scale(coffee,(SQ_SIZE, SQ_SIZE))

class Coffee():
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def drawCoffee(self, screen):
        screen.blit(coffee, (self.x, self.y))
        

def spawnCoffee(coordinates):
    used_coordinates = []
    for x,y in coordinates:
        restX = x % 35
        restY = y % 35
        fullX = x // 35
        fullY = y // 35
        used_coordinates.append((fullX*35, fullY*35))
        if restX > 0:
            used_coordinates.append((fullX * 35 + 35, fullY * 35))
        if restY > 0:
            used_coordinates.append((fullX * 35, fullY * 35 + 35))

    if len(used_coordinates) < 300:
        while True:
            rx = randint(0,19)*35
            ry = randint(0,19)*35
            if (rx,ry) not in used_coordinates:
                return Coffee(rx, ry)
    else:
        free_coordinates = []
        for x in range(20):
            for y in range(20):
                if (x*35,y*35) not in used_coordinates:
                    free_coordinates.append(x*35,y*35)
        nx, ny = choice(free_coordinates)
        return Coffee(nx, ny)

