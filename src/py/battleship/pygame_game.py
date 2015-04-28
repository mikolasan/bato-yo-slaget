from battleship.Game import Game
from battleship.pygame_player import *
from battleship.pygame_elements import *

class PyGame_Game(Game):
    
    ship_setup = False
    
    def __init__(self):
        self.aim = Aim()
        self.aim_group = sprite.Group()
        self.aim_group.add(self.aim)
    
    def start(self):
        Game.start(self,10, 1)
        
    def initialize(self):
        pygame.key.set_repeat(500, 30)      
    
    def place_ship(self):
        board = self.curr_player.board
        ship = board.managed_ship
        board.place_ship(ship)
        
        self.curr_player.setup_next_ship()
        
        
    def rotate_ship(self):
        board = self.curr_player.board
        ship = board.managed_ship
        board.managed_ship = board.rotate_ship(ship)
    
    def move_ship(self, course):
        board = self.curr_player.board
        ship = board.managed_ship
        board.move_ship(ship, course)
            
    def move_aim(self, course):
        if course == 'up':
            self.aim.dy -= 1
        elif course == 'down':
            self.aim.dy += 1
        elif course == 'left':
            self.aim.dx -= 1
        elif course == 'right':
            self.aim.dx += 1

    def hit(self):
        h = self.curr_opponent.on_fire(self.aim.x, self.aim.y)
                    
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
        
