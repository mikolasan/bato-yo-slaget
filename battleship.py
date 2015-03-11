#!/usr/bin/python
# vim: set fileencoding=utf-8

import random

class OutofboardError(Exception):
    pass

class ShipAlreadyThere(Exception):
    pass

class TooManyPlayers(Exception):
    pass



class Cell(object):

    # states = set(['fog','empty', 'ship', 'miss', 'near', 'fate'])
    
    def __init__(self, x, y, state = None, ship = None):
        self.x = x
        self.y = y
        self.state = None
        if state:
            self.state = state
        self.ship = None
        if ship:
            self.ship = ship

    def set_state(self, state):
        self.state = state
        
            
class Ship(object):
    names = ['Boat', 'Submarine', 'Destroyer', 'Battleship', 'Carrier']
    
    def __init__(self, cells = []):
        self.cells = cells
        self.length = len(cells)
        try:
            self.name = self.names[self.length - 1]
        except IndexError:
            self.name = "UFO"
        self.area = self.find_area()

    def create(self, start_x, start_y, length, direction):
        self.length = length
        self.cells = [None] * length
        for i in range(0, length):
            if direction == "V":
                x = start_x
                y = start_y + i
            elif direction == "H":
                x = start_x + i
                y = start_y
            self.cells[i] = Cell(x, y, 'ship')
        try:
            self.name = self.names[self.length - 1]
        except IndexError:
            self.name = "UFO"
        self.area = self.find_area()
    
    def find_area(self):
        area = []
        for c in self.cells:
            #print c.x, c.y
            area += self.get_near(c, 1, self.cells + area)
        return area

                    
    def get_near(self, center, radius, engaged = None):
        near = []
        if not engaged:
            engaged = [center]
        else:
            engaged = engaged[:]
            engaged.append(center)
        
        for x in range(center.x + radius, center.x - radius - 1, -1):
            for y in range(center.y + radius, center.y - radius - 1, -1):
                new = True
                for e in engaged:
                    if x == e.x and y == e.y:
                        new = False
                        break
                if new:
                    cell = Cell(x, y, 'near')
                    near.append(cell)
                    engaged.append(cell)
                    
        return near
        
        

class Board(object):

    def __init__(self, size):
        """Init squared field"""
        self.board = {}
        self.ships = []
        self.size = size
        for i in range(size):
            for j in range(size):
                self.board[(i,j)] = Cell(i, j, 'empty')

    def setup_ship(self, size, rand = True):
        '''Places a ship of ship_size on the board for either a human, if human
        is true, or a computer player.'''
        
        if rand:
            #randomize computer player's ships
            x = random.randint(0, self.size)
            y = random.randint(0, self.size)
            orientation = random.randint(0, 1) == 0 and "V" or "H"
        else:
            self.pretty_print()
            x = raw_input('What is the x co-ordinate for your ' + str(size) + 
                          '? ')
            y = raw_input('What is the y co-ordinate for your ' + str(size) + 
                          '? ')
            orientation = raw_input('''If you wish to place the ship 
            vertically, enter V. For a horizontl ship, enter H. ''')
            try:
                x, y, orientation = int(x), int(y), str(orientation)
                # Verifies the input values are integers
            except Exception:
                self.setup_ship(size, random)
                
        cells = [None] * size
        for i in range(0, size):
            if orientation == "V":
                x_ = x
                y_ = y + i
            elif orientation == "H":
                x_ = x + i
                y_ = y
            cells[i] = Cell(x_, y_, 'ship')
        if not self.add_ship(cells):
            self.setup_ship(size, random)
        

    def add_ship(self, cells):
        ship = Ship(cells)
        
        # check collisions
        collision = []
        for s in self.ships:
            for full in (s.cells + s.area):
                for new in (ship.cells + ship.area):
                    if full.x == new.x and full.y == new.y:
                        collision.append(new)
        
        if len(collision) == 0:
            self.ships.append(ship)
            for c in cells:
                self.board[(c.x, c.y)].set_state('ship')
                self.board[(c.x, c.y)].ship = ship
            return True
        return False

    def pretty_print(self):
        s = ""
        for y in range(self.size):
            for x in range(self.size):
                if self.board[(x,y)].state == 'empty':
                    s += "."
                elif self.board[(x,y)].state == 'ship':
                    s += "x"
                elif self.board[(x,y)].state == 'near':
                    s += "_"
            s += "\n"
        print s


class Player(object):
    """The map, ship and firing mechanism for a player of the game battleship.
    """

    def __init__(self, human = False):
        '''Initializes a player's basic requirements'''
        self.human = human
        self.name ='Bot'
        self.score = 0
        
    def init_board(self, size, fleet):
        self.board = Board(size)
        
        human = self.human
        if human:
            random = -1
            while random != 1 and random != 0:
                random = input("Do you want to place your own ship?(1-Yes, 0-Random):")
            if random == 0:
                human = False

        for s in range(0, len(fleet)):
            ship_size = s + 1
            count = fleet[s]
        
            while count > 0:
                if self.board.setup_ship(ship_size, not human):
                    count -= 1


    def set_human():
        self.human = True


    def fire(self):
        if not self.human:
            #checks to see if the current player should be a computer.
            x = random.randint(0,self.size)
            y = random.randint(0,self.size)
        else:
            x = raw_input('What is the x-coordinate you wish to fire on? ')
            y = raw_input('What is the y-coordinate you wish to fire on? ')
        try:
            x, y = int(x), int(y)
            # verifies that x and y are valid integers.
        except Exception:
            self.fire()
            
        self.fire_helper(x,y)

    def fire_helper(self,x,y):
        '''Fires at coordinates (x,y) on opponent'''

        if x > self.size or y > self.size:
            #Checks to make sure that x and y and in the scope of the board.
            print 'Out of bounds'
            self.fire()
        elif self.opponents_board.get((x,y)) != '?':
            #Checks if the current spot has been chosen.
            print 'That coordinate has been fired already'
            self.fire()
        elif (self.opponent.board.get((x,y)) == '.' or 
              self.opponent.board.get((x,y)) == 'x'):
            #The player has hit an s and missed.
            print 'Target missed'
            self.opponents_board[(x,y)] = 'x'
            self.opponent.board[(x,y)] = 'x'
        else:
            #A player's ship has been hit! Mark it on the board.
            ship_name_list = ['Destroyer','Frigate','Battleship','Carrier']
            
            print ("Hit enemy's " + \
                   ship_name_list[self.opponent.board.get((x,y)) - 2])
            self.score -= 1
            self.opponents_board[(x,y)] = \
                self.opponent.board.get((x,y))
            self.opponent.board[(x,y)] = 'x'

    def turn(self):
        raw_input(self.name + ''''s turn''' + ' push enter to continue')
        if not self.human and self.opponent.human:
            pass
        else:
            print 'Your board:'
            self.print_map(True)
            print '''Your view of your opponent's board:'''
            self.print_map(False)
            # Print your view of the opponents map.
        self.fire()
        for n in range(20):
            print ''

    
    
class Game(object):

    def __init__(self):
        print "Welcome on board"

        size = 0
        while size < 1:
            size = int(input("What size board would you like? "))
            
        fleet_settings = self.define_ships()
        
        n_players = -1
        while n_players > 2 or n_players < 0:
            n_players = int(input("State the number of human players(0,1 or 2): "))

        self.players = {}
        for i in range(0, 2):
            self.players[i] = Player()
            if n_players > i:
                self.players[i].set_human()
                self.players[i].name = raw_input('What is your name player ' + (i+1) + '? ')
            self.players[i].init_board(size).setup_ships(fleet_settings)


        self.game_over = False
        self.curr_player = self.players[0]
        self.curr_opponent = self.players[1]
        

    def define_ships(self, default_settings = True):
        settings = [4, 3, 2, 1, 0]
        if not default_settings:
            for i in range(0, 5):
                try:
                    settings[i] = int(raw_input('State an amount of boats with length ' + str(i + 1) + ': '))
                except Exception:
                    settings = self.define_ships()
        return settings
                   
    def play(self):
        for n in range(40):
            print ''
        while not self.game_over:
            self.curr_player.turn()
            self.game_over = (not self.curr_player.score)
            self.curr_opponent, self.curr_player = (self.curr_player, 
                                                    self.curr_opponent)
            #Swap player's seats.
        self.curr_opponent.print_map(False)
        print self.curr_opponent.name + ''' wins!'''



#game = Game()
#game.play()



