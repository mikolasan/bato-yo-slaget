import pygame
from .Cell import Cell
from battleship.ui.colors import Colors


class PyCell(Cell, pygame.sprite.Sprite):

    # {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    size = 32
    padding = 2
    cx = 0
    cy = 0

    def __init__(self, x, y, state, cx, cy):
        Cell.__init__(self, x, y, state)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.cx = cx
        self.cy = cy
        self._draw()

    def update(self):
        self._draw()

    def _draw(self):
        self.rect.left = self.cx + (self.size + self.padding) * self.x
        self.rect.top = self.cy + (self.size + self.padding) * self.y

        if self.state == 'ship':
            self.image.fill(Colors.player_c)
        elif self.state == 'empty':
            self.image.fill(Colors.empty_c)
        elif self.state == 'near':
            self.image.fill(Colors.near_c)
        elif self.state == 'fate':
            self.image.fill(Colors.fate_c)
        elif self.state == 'fog':
            self.image.fill(Colors.fog_c)
        elif self.state == 'miss':
            self.image.fill(Colors.miss_c)
        elif self.state == 'new':
            self.image.fill(Colors.new_c)
