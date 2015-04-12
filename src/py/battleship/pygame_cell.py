import pygame
from Cell import Cell

class PyGame_Cell(Cell, pygame.sprite.Sprite):

	 # {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    
    player_c = (54, 85, 99) # metallic blue
    #(250,250,250) # white
    empty_c = (123, 173, 196)# grey
    near_c = (137, 218,218) # light blue
    fate_c = (241,122,64) # orange
    fog_c = (100, 114, 127) # violet
    new_c = (250, 0, 0)
    
    size = 32
    padding = 2
    
    def __init__(self, x, y, state, cx, cy):
        Cell.__init__(self, x, y, state)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.size, self.size))
        self._draw()
        self.rect = self.image.get_rect()
        self.rect.left = cx + (self.size + self.padding) * self.x
        self.rect.top = cy + (self.size + self.padding) * self.y

    def update(self):
        self._draw()
    
    def _draw(self):
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
            self.image.fill(self.empty_c)
        elif self.state == 'new':
            self.image.fill(self.new_c)
