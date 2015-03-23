
from pygame.sprite.Sprite import pySprite
from pygame.Surface import pySurface
from battleship.Ship import Ship


class Ship(pygame.sprite.Sprite):
    x = 391
    y = 291

    x_shift = 0
    y_shift = 0

    color = ((200,0,0))
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        rotate = 0

        pySprite.__init__(self)
        self.image = pySurface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.x_shift
        self.rect.y += self.y_shift

    def rotate(self):
        self.w, self.h = self.h, self.w
        self.image = pySurface((self.w, self.h))
        self.image.fill(self.color)
