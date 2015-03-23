
from pygame.sprite.Sprite import pySprite
from pygame.Surface import pySurface
from battleship.Cell import Cell


class PyGame_Cell(Cell, pygame.sprite.Sprite):

    color1 = (98, 238,154)
    color2 = (24, 216,235)
    color3 = (250,250,250)
    color4 = (15,25,71)

    def __init__(self, typ):
        self.typ = typ
        pySprite.__init__(self)
        self.image = pySurface((32, 32))
        if self.typ == 'p':
            self.image.fill(self.color1)
        elif self.typ == 'c':
            self.image.fill(self.color2)
        elif self.typ == 'd' or self.typ == 'o':
            self.image.fill(self.color3)
        elif self.typ == 'g':
            self.image.fill(self.color4)
        elif self.typ == 'dead':
            self.image.fill((0,0,0))
        elif self.typ == 'damaged':
            
        self.rect = self.image.get_rect()

    
    def update(self):
        if self.typ == 'p':
            self.image.fill(self.color1)
        elif self.typ == 'c':
            self.image.fill(self.color2)
        elif self.typ == 'd' or self.typ == 'o':
            self.image.fill(self.color3)
        elif self.typ == 'g':
            self.image.fill(self.color4)
        elif self.typ == 'dead':
            self.image.fill((0,0,0))
        elif self.typ == 'damaged':
            self.image.fill((50,50,50))
