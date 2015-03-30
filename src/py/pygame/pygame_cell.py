
from pygame.sprite.Sprite import pySprite
from pygame.Surface import pySurface
from battleship.Cell import Cell


class PyGame_Cell(Cell, pygame.sprite.Sprite):

	 # {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    
	# color1 = (98, 238,154)
    # color2 = (24, 216,235)
    # color3 = (250,250,250)
    # color4 = (15,25,71)
	
	player_c = (98, 238,154)
    bot_c = (24, 216,235)
    near_c = (250,250,250)
    fate_c = (15,25,71)
	
	self.size = 32
    
	def __init__(self, state):
        self.state = state
        pySprite.__init__(self)
        self.image = pySurface((self.size, self.size))
        if self.state == 'p':
            self.image.fill(self.player_c)
        elif self.state == 'c':
            self.image.fill(self.bot_c)
        elif self.state == 'd' or self.state == 'o':
            self.image.fill(self.near_c)
        elif self.state == 'g':
            self.image.fill(self.fate_c)
        elif self.state == 'dead':
            self.image.fill((0,0,0))
        elif self.state == 'damaged':
            self.image.fill((50,50,50))
			
        self.rect = self.image.get_rect()

    
    def update(self):
        if self.state == 'p':
            self.image.fill(self.player_c)
        elif self.state == 'c':
            self.image.fill(self.bot_c)
        elif self.state == 'd' or self.state == 'o':
            self.image.fill(self.near_c)
        elif self.state == 'g':
            self.image.fill(self.fate_c)
        elif self.state == 'dead':
            self.image.fill((0,0,0))
        elif self.state == 'damaged':
            self.image.fill((50,50,50))
