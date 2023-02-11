'''
This file contains Snake class.
'''

import pygame as p

SQ_SIZE = 35


class Snake():
    def __init__(self):
        self.length = 1
        self.direction = 'down'
        self.coordinates = [(0,0)]


    def drawSnake(self,screen):
        snake_box = p.image.load("images/snake_box.png")
        snake_head = p.image.load("images/snake_head.png")
        snake_tail = p.image.load("images/snake_tail.png")
        snake_box = p.transform.scale(snake_box,(SQ_SIZE, SQ_SIZE))
        snake_head = p.transform.scale(snake_head,(SQ_SIZE, SQ_SIZE))
        snake_tail = p.transform.scale(snake_tail,(SQ_SIZE, SQ_SIZE))
        for i in range(self.length):
            if i == 0 and self.length > 1:
                if self.direction == 'down':
                    snake_head = p.transform.rotate(snake_head, 0)
                elif self.direction == 'right':
                    snake_head = p.transform.rotate(snake_head, 90)
                elif self.direction == 'up':
                    snake_head = p.transform.rotate(snake_head, 180)
                elif self.direction == 'left':
                    snake_head = p.transform.rotate(snake_head, 270)
                screen.blit(snake_head, self.coordinates[i])
            elif self.length > 1 and i == self.length - 1:
                lx, ly = self.coordinates[i-1]
                x, y = self.coordinates[i]
                if lx > x:
                    snake_tail = p.transform.rotate(snake_tail, 90)
                elif lx < x:
                    snake_tail = p.transform.rotate(snake_tail, 270)
                elif ly > y:
                    snake_tail = p.transform.rotate(snake_tail, 0)
                else:
                    snake_tail = p.transform.rotate(snake_tail, 180)
                screen.blit(snake_tail, self.coordinates[i])
            else:
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
    

