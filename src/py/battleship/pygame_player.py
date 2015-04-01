from battleship.Player import Player
from battleship.pygame_board import *

class PyGame_Player(Player):

    # where boards can be placed
    places = [(10, 10), (380, 300)]

    def __init__(self, player_id, human = False):
        Player.__init__(self, human)
        self._id = player_id

    def composite(self, size):
        x, y = self.places[self._id][0], self.places[self._id][1]
        if self.human:
            return PyGame_Board(size, x, y)
        else:
            return PyGame_Enemy_Board(size, x, y)
        

