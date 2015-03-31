import pygame
from battleship.Board import Board
from battleship.pygame_cell import *

class PyGame_Board(Board, pygame.sprite.Sprite):

    color = (15,25,71) # dark blue
    
    
    def __init__(self, size = 10, hidden = False, cX = 0, cY = 0):
        self.cx = cX
        self.cy = cY
        
        Board.__init__(self, size, hidden)
        pygame.sprite.Sprite.__init__(self)
        
        cell = PyGame_Cell.size + PyGame_Cell.padding
        side = cell * self.size + PyGame_Cell.padding
        self.image = pygame.Surface((side, side))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.left = cX - PyGame_Cell.padding
        self.rect.top = cY - PyGame_Cell.padding
        self.draw_list = self.get_draw_list()
        #self.render = pygame.sprite.LayeredUpdates(self.draw_list)

    def composite(self, x, y, state):
        return PyGame_Cell(x, y, state, self.cx, self.cy)

    def get_draw_list(self):
        return [self] + [(v) for k, v in self.board.iteritems()]

    def update(self):
        self.image.fill(self.color)
        self.draw_list = self.get_draw_list()
        #self.render = pygame.sprite.LayeredUpdates(self.draw_list)

