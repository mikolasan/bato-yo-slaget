import pygame
from .Cell import Cell


class PyCell(Cell, pygame.sprite.Sprite):

	 # {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    
    player_c = (54, 85, 99) # metallic blue
    #(250,250,250) # white
    empty_c = (123, 173, 196) # grey
    near_c = (87, 142, 132) # green-blue
    fate_c = (139, 64, 116) # purple
    fog_c = (100, 114, 127) # violet
    miss_c = (179, 204, 220)
    new_c = (250, 0, 0)
    
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
            self.image.fill(self.player_c)
        elif self.state == 'empty':
            self.image.fill(self.empty_c)
        elif self.state == 'near':
            self.image.fill(self.near_c)
        elif self.state == 'fate':
            self.image.fill(self.fate_c)
        elif self.state == 'fog':
            self.image.fill(self.fog_c)
        elif self.state == 'miss':
            self.image.fill(self.miss_c)
        elif self.state == 'new':
            self.image.fill(self.new_c)
