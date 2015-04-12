import pygame
from battleship.Board import *
from battleship.pygame_cell import *

        
class PyGame_Board(Board, pygame.sprite.Sprite):

    color = (15,25,71) # dark blue
    
    def __init__(self, size = 10, cX = 0, cY = 0):
        self.cx = cX
        self.cy = cY
        
        Board.__init__(self, size)
        pygame.sprite.Sprite.__init__(self)
        self._draw()
        
    def _draw(self):
        cell = PyGame_Cell.size + PyGame_Cell.padding
        side = cell * self.size + PyGame_Cell.padding
        self.image = pygame.Surface((side, side))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.left = self.cx - PyGame_Cell.padding
        self.rect.top = self.cy - PyGame_Cell.padding
        self.draw_list = self.get_draw_list()
        

    def composite(self, x, y, state):
        return PyGame_Cell(x, y, state, self.cx, self.cy)

    def get_draw_list(self):
        managed_ship = []
        if self.managed_ship:
             managed_ship = self.managed_ship.cells
        return [self] + [(v) for k, v in self.board.iteritems()] + managed_ship

    def update(self):
        self.image.fill(self.color)
        self.draw_list = self.get_draw_list()
        

class PyGame_Enemy_Board(Enemy_Board, PyGame_Board):
    
    def __init__(self, size = 10, cX = 0, cY = 0):
        self.cx = cX
        self.cy = cY
        self.managed_ship = None
        Enemy_Board.__init__(self, size)
        pygame.sprite.Sprite.__init__(self)
        PyGame_Board._draw(self)

