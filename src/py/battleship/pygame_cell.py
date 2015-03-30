import pygame
from Cell import Cell

class PyGame_Cell(Cell, pygame.sprite.Sprite):

	 # {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    
    player_c = (15,25,71) # dark blue
    empty_c = (24, 216,235) # blue
    near_c = (98, 238,154) # green
    fate_c = (250,250,250) # black

    size = 32
    padding = 2
    
    def __init__(self, x, y, state):
        Cell.__init__(self, x, y, state)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.size, self.size))
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.left = (self.size + self.padding) * self.x
        self.rect.top = (self.size + self.padding) * self.y

    def update(self):
        self.draw()    
    
    def draw(self):
        if self.state == 'ship':
            self.image.fill(self.player_c)
        elif self.state == 'empty':
            pass
            #self.image.fill(self.empty_c)
        elif self.state == 'near':
            self.image.fill(self.near_c)
        elif self.state == 'fate':
            self.image.fill(self.fate_c)
