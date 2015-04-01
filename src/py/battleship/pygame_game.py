from battleship.Game import Game
from battleship.pygame_player import *
from battleship.pygame_elements import *

class PyGame_Game(Game):
    
    def __init__(self):
        Game.__init__(self, 10, 1)
        

    def composite(self):
        player_id = len(self.players)
        return PyGame_Player(player_id)

    def get_sprites(self):
        sprites = []
        for p in self.players:
            sprites = sprites + p.board.draw_list
        return sprites

