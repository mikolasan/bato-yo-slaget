import pygame
from .Board import Board, EnemyBoard
from .PyCell import PyCell


class PyBoard(Board, pygame.sprite.Sprite):

    color = (15, 25, 71)  # dark blue

    def __init__(self, size=10, cX=0, cY=0):
        self.cx = cX
        self.cy = cY

        Board.__init__(self, size)
        pygame.sprite.Sprite.__init__(self)
        self._draw()

    def _draw(self):
        cell = PyCell.size + PyCell.padding
        side = cell * self.size + PyCell.padding
        self.image = pygame.Surface((side, side))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.left = self.cx - PyCell.padding
        self.rect.top = self.cy - PyCell.padding
        self.draw_list = self.get_draw_list()

    def composite(self, x, y, state):
        return PyCell(x, y, state, self.cx, self.cy)

    def get_draw_list(self):
        managed_ship = []
        if self.managed_ship:
            managed_ship = self.managed_ship.cells
        return [self] + [(v) for k, v in self.board.items()] + managed_ship

    def update(self):
        self.image.fill(self.color)
        self.draw_list = self.get_draw_list()


class PyEnemyBoard(EnemyBoard, PyBoard):
    def __init__(self, size=10, cX=0, cY=0):
        self.cx = cX
        self.cy = cY
        self.managed_ship = None
        EnemyBoard.__init__(self, size)
        pygame.sprite.Sprite.__init__(self)
        PyBoard._draw(self)
