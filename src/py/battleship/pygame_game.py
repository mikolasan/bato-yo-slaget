from battleship.Game import Game
from battleship.pygame_player import *
from battleship.pygame_elements import *

class PyGame_Game(Game):
    
    def __init__(self):
        Game.__init__(self, 10, 1)
        
        self.aim = Aim()
        self.aim.rect.x = 380
        self.aim.rect.y = 300
        self.aim_group = sprite.Group()
        self.aim_group.add(self.aim)
        
        self.aim_dx = 0
        self.aim_dy = 0
        
    def move_aim(self, course):
        if course == 'up':
            self.aim.rect.y -= 34
        elif course == 'down':
            self.aim.rect.y += 34
        elif course == 'left':
            self.aim.rect.x -= 34
        elif course == 'right':
            self.aim.rect.x += 34
    
#        if course == 'up':
#            self.aim_dy -= 34
#        elif course == 'down':
#            self.aim_dy += 34
#        elif course == 'left':
#            self.aim_dx -= 34
#        elif course == 'right':
#            self.aim_dx += 34
            
    def composite(self):
        player_id = len(self.players)
        return PyGame_Player(player_id)

    def get_sprites(self):
        sprites = []
        for p in self.players:
            sprites = sprites + p.board.draw_list
        if self.curr_player.human:
            sprites.append(self.aim_group)
        return sprites
        

