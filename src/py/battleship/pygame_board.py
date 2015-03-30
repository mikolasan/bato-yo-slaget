import pygame
from battleship.Board import Board
from battleship.pygame_cell import *

class PyGame_Board(Board, pygame.sprite.Sprite):

    color = (128,0,137)
    
    def __init__(self, size = 10, cX = 0, cY = 0):
        Board.__init__(self, size)
        pygame.sprite.Sprite.__init__(self)
        
        cell = PyGame_Cell.size + PyGame_Cell.padding
        self.image = pygame.Surface((cell * self.size, cell* self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
        self.draw_list = [self]
        for i in range(size):
            for j in range(size):
                self.draw_list.append(PyGame_Cell(i, j, 'empty'))
        self.render = pygame.sprite.LayeredUpdates(self.draw_list)
        
        
    def update(self):
        self.image.fill(self.color)

