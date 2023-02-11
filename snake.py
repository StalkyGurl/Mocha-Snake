'''
This file contains Snake class.
'''

import pygame as p

SQ_SIZE = 35

snake_box = p.image.load("images/snake_box.png")
snake_box = p.transform.scale(snake_box,(SQ_SIZE, SQ_SIZE))

class Snake():
    def __init__(self):
        self.length = 1
        self.direction = 'down'
        self.coordinates = [(0,0)]


    def drawSnake(self,screen):
        for i in range(self.length):
            screen.blit(snake_box, self.coordinates[i])

    
    def moveSnake(self, eaten = False):
        x, y = self.coordinates[0][0], self.coordinates[0][1]
        if not eaten:
            self.coordinates.pop()
        if self.direction == 'down':
            self.coordinates.insert(0,(x, (y + SQ_SIZE) % 700))
        elif self.direction == 'up':
            self.coordinates.insert(0,(x, (y - SQ_SIZE) % 700))
        elif self.direction == 'left':
            self.coordinates.insert(0,((x - SQ_SIZE) % 700, y))
        elif self.direction == 'right':
            self.coordinates.insert(0,((x + SQ_SIZE) % 700, y))

    
    def endGame(self):
        x, y = self.coordinates[0][0], self.coordinates[0][1]
        for nx, ny in self.coordinates[1:]:
            if x == nx and y == ny:
                return True
        return False
    

