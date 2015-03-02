import random

class OutofboardError(Exception):
    pass

class ShipAlreadyThere(Exception):
    pass

class TooManyPlayers(Exception):
    pass

class Cell(object):
    # states = set(['fog','empty', 'ship', 'miss', 'near', 'fate'])
    
    def __init__(self, x, y, state, ship)
        self.x = x
        self.y = y
        self.state = None
        if state:
            self.state = state
        self.ship = None
        if ship:
            self.ship = ship
            
class Ship(object):
    def __init__(self, field, cells)
        self.cells = cells
        self.area = {}
        for c in cells:
            x = c[0]
            y = c[1]
            if x - 1 >= 0:
                self.area.append((x-1, y))
            if x + 1 <= self.field.size
        self.length = len(cells)

class Board(object):
    def __init__(self, size)
        """Init squared field"""
        for i in range(size):
            for j in range(size):
                self.board[(i,j)] = Cell(i, j, 'empty')
                
    def check_collisions(self, ship)
        for s in self.ships:
            for

class Battleship(object):
    """The game board of battleShip"""

    def __init__(self, size, players):
        """Create two boards each with the size of size*size and number of human
        players, player."""
        
        self.size = size
        self.players = players
        self.player1 = player(self.size)
        self.player2 = player(self.size)
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1
        self.curr_opponent = self.player2
        self.curr_player = self.player1
        self.player1.name = 'Player One'
        self.player2.name = 'Player Two'
        self.select_ships()
        self.startup()
        self.game_over = False
        self.play()

    

        
class Player(object):
    """The map, ship and firing mechanism for a player of the game battleship.
    """

    def __init__(self):
        '''Initializes a player's basic requirements'''
        self.human = False
        self.name ='Bot'
        self.score = 0
        
    def init_board(self, size)
        self.board = Board(size)

    def set_human()
        self.human = True
        
    def get_reserved_cells(self, ship)
        '''Description'''
        pass

    def place_ships(self, size, x, y, orientation):
        '''Place ship of size, size, starting at position (x,y) and oriented
        vertically (oreitnation = 0) or horizontally (orientation = 1).'''
        self.check_collisions(size, x, y, orientation)
        # Checks to make sure the ship doesn't lie outside the board and that
        # no ships have been placed on those spots.
        if not orientation:
            min_x = max(x - 1, 0)
            max_x = min(x + size + 1, self.size - 1)
            min_y = max(y - 1, 0)
            max_y = min(y + size + 1, self.size - 1)
            for x_ in range(min_x, max_x):
            if x <= x_ and x_ <= x + size):
                self.board[(x,y)] = size
            else:
                self.board[(x,y)] = '_'
        elif orientation:
            for y in range(y, y + size):
                self.board[(x,y)] = size
        for c in get_reserved_cells(ship):
            self.board[c] = '_'

    def check_collisions(self, size, x, y, orientation):
        '''Checks to make sure the ship doesn't lie outside the board and that
        no ships have been placed on those spots.'''
        if not orientation:
            # orientation == 1; ship will be oriented horizontally
            if self.size < (x + size) or self.size < y:
                raise OutofboardError()
            min_x = max(x - 1, 0)
            max_x = min(x + size + 1, self.size - 1)
            for x in range(min_x, max_x):
                if self.board.get((x,y)) != '.':
                    raise ShipAlreadyThere()
        elif orientation:
            # orientation == 0; ship will be oriented vertically
            if self.size < (y + size) or self.size < x:
                raise OutofboardError()
            min_y = max(y - 1, 0)
            max_y = min(y + size + 1, self.size - 1)
            for y in range(min_y, max_y):
                if self.board.get((x,y)) != '.':
                    raise ShipAlreadyThere()

    def print_map(self, which_map):
        '''If which_map is true, print your map, else print your opponent's 
        map'''
        row = '   '
        for i in range(self.size):
            row += str(i) + (3-len(str(i)))*' '
        print row
        row = ''
        for i in range(self.size):
            row += str(i) + (3-len(str(i)))*' '
            for j in range(self.size):
                if which_map:
                    row += str(self.board[(j,i)]) + 2* ' '
                else:
                    row += str(self.opponents_board[(j,i)]) + 2* ' '
            print row
            row = ''

    def player_setup(self, human):
        '''Sets up the player's ships for either a human if human is true, else
        sets up the computer player's ships.'''
        self.human = human
        if human:
            self.name = raw_input('What is your name ' + self.name + '? ')
            random = input("Do you want to place your own ship?(1-Yes, 0-Random):")
            while random != 1 and random != 0:
                random = input("Do you want to place your own ship?(1-Yes, 0-Random):")
            if random == 0:
                human = False
        for ship_size in self.select_ships:
            #changing the number in the above bracket changes the number of
            #ships used in the game.
            self.ship_setup(ship_size, human)

    def ship_setup(self, ship_size, human):
        '''Places a ship of ship_size on the board for either a human, if human
        is true, or a computer player.'''
        ships = ['Destroyer', 'Submarine', 'Battleship', 'Carrier']
        if human:
            self.print_map(True)
            x = raw_input('What is the x co-ordinate for your ' + 
                          ships[ship_size -2] + ' of size ' + str(ship_size) + 
                          '? ')
            y = raw_input('What is the y co-ordinate for your ' + 
                          ships[ship_size -2] + ' of size ' + str(ship_size) + 
                          '? ')
            orientation = raw_input('''If you wish to place the ship 
            vertically, enter 1. For a horizontl ship, enter 0. ''')
            try:
                x,y,orientation = int(x), int(y),int(orientation)
                # Verifies the input values are integers
            except Exception:
                self.ship_setup(ship_size, human)
        else:
            #randomize computer player's ships
            x = random.randint(0, self.size)
            y = random.randint(0, self.size)
            orientation = random.randint(0, 1)
        try: 
            self.place_ships(ship_size, x, y, orientation)
        except OutofboardError:
            # The player tried to place the ship out of bounds.
            self.ship_setup(ship_size, human)
        except ShipAlreadyThere:
            #A ship occupies the current spot.
            self.ship_setup(ship_size, human)

    def fire(self):
        if not self.human:
            #checks to see if the current player should be a computer.
                x = random.randint(0,self.size)
                y = random.randint(0,self.size)
        else:
            x = raw_input('What is the x-coordinate you wish to fire on? ')
            y = raw_input('What is the y-coordinate you wish to fire on? ')
        try:
            x,y = int(x), int(y)
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
    def __init__(self)
        print "Welcome on board"

        size = 0
        while size < 1:
            size = int(input("What size board would you like? "))
            
        n_players = -1
        while n_players > 2 or n_players < 0:
            n_players = int(input("State the number of human players(0,1 or 2): "))

        self.players = {}
        for i in range(0, 2):
            self.players[i] = Player()
            self.players[i].init_board(size)
            if n_players > i:
                self.players[i].set_human()

        self.game_over = False
        self.curr_player = self.players[0]
        self.curr_opponent = self.players[1]
        self.select_ships()

    def select_ships(self):
        two = raw_input('Captain please state the number of destroyers(length 2): ')
        three = raw_input('Captain please state the number of frigates(length 3): ')
        four = raw_input('Captain please state the number of battleships(length 4): ')
        five = raw_input('Captain please state the number of carriers(length 5): ')
        try:
            two, three, four, five = int(two), int(three), int(four), int(five)
            # verifies that they are valid integers.
        except Exception:
            self.select_ships()
        self.player1.score = 2*two + 3*three + 4*four + 5*five
        self.player2.score = 2*two + 3*three + 4*four + 5*five
        self.player1.select_ships = two*[2] + three*[3] + four*[4] + five*[5]
        self.player2.select_ships = two*[2] + three*[3] + four*[4] + five*[5]

                   
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

     
game = Game()
game.play()



