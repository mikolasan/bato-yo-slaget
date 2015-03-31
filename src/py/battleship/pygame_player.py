from battleship.Player import Player
from battleship.pygame_board import *

class PyGame_Player(Player):

    # where boards can be placed
    places = [(10, 10), (380, 300)]

    def __init__(self, player_id, human = False):
        Player.__init__(self, human)
        self._id = player_id

    def composite(self, size, hidden):
        x, y = self.places[self._id][0], self.places[self._id][1]
        return PyGame_Board(size, hidden, x, y)

