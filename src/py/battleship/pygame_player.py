from battleship.Player import Player
from battleship.pygame_board import *
from battleship.pygame_elements import *

class PyGame_Player(Player):

    # where boards can be placed
    places = [(10, 10), (380, 300)]
    stage = None
    
    def __init__(self, player_id, human = False):
        Player.__init__(self, human)
        self._id = player_id

    def composite(self, size):
        x, y = self.places[self._id][0], self.places[self._id][1]
        if self.human:
            return PyGame_Board(size, x, y)
        else:
            return PyGame_Enemy_Board(size, x, y)
        
    def init_board(self, size, fleet, random = -1):
        self.board = self.composite(size)
        self.fleet = fleet
        if self.human:
            print("setup modal dialog")
            Modal_dialog._title = "Auto ships"
            Modal_dialog._answers = ['Yeah!', "Ill do it"]
            Modal_dialog.sender = self
            Modal_dialog.callback = self.on_dialog_done
            Modal_dialog._new = True
            self.stage = "planning"
        else:
            self.setup_ships(fleet, False)

    def on_dialog_done(self, answer):
        self.manual_setup = (answer == 1)
        if self.manual_setup:
            self.setup_next_ship()
        else:
            self.setup_ships(self.fleet, False)
            self.stage = "scanning"
        
    def setup_next_ship(self, set_prev = False):
        print("setup player ships", self.fleet)
        patch_prev = set_prev
        for s in range(0, len(self.fleet)):
            ship_size = s + 1
            
            if self.fleet[s] > 0 and patch_prev:
                self.fleet[s] -= 1
                patch_prev = False
            
            if self.fleet[s] > 0:
                print(ship_size)
                last_x, last_y = 0, 0
                last_direction = "H"
                if self.board.managed_ship:
                    cell_0 = self.board.managed_ship.cells[0]
                    last_x = cell_0.x
                    last_y = cell_0.y
                    last_direction = self.board.managed_ship.direction
                self.board.managed_ship = self.board.create_ship(last_x, last_y, ship_size, last_direction, "new", True)
                self.board.managed_ship = self.board.check_bounds(self.board.managed_ship)
                return True
        return False

