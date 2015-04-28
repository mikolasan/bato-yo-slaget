#!/usr/bin/python
# vim: set fileencoding=utf-8


import random
from Cell import Cell
from Ship import Ship

class Board(object):

    def __init__(self, size):
        """Init squared field"""
        self.board = {}
        self.ships = []
        self.managed_ship = None
        self.size = size
        for i in range(self.size):
            for j in range(self.size):
                self.board[(i,j)] = self.composite(i, j, 'empty')

    def composite(self, x, y, state):
        return Cell(x, y, state)

    def get(self, x, y):
        return self.board[(x, y)]
    
    def reveal(self, x, y):
        cell = self.board[(x, y)]
        # escape repeated hits
        if (cell.state == 'fate' or
                cell.state == 'miss' or
                cell.state == 'near'):
            return cell
        
        if cell.ship:
            cell.state = 'fate'
            
            ship = cell.ship
            print ("Hit " + ship.name)
            
            ship.length -= 1
            if ship.length == 0:
                for c in ship.cells:
                    c.ship = None
                for a in ship.area:
                    size = self.size
                    if a.x >=0 and a.x < size and a.y >=0 and a.y < size:
                        cell = self.board[(a.x, a.y)]
                        if cell.state == 'empty' or cell.state == 'fog':
                            cell.state = 'near'
                self.ships.remove(ship)
            #cell.ship = None
            self.board[(x, y)].ship = None
        else:
            print 'Target missed'
            cell.state = 'miss'
        
        self.debug_print()    
        return cell
        
    def setup_ship(self, size, rand = True):
        '''Places a ship of ship_size on the board for either a human, if human
        is true, or a computer player.'''
        
        #self.pretty_print()
        
        if rand:
            #randomize computer player's ships
            x = random.randint(0, self.size)
            y = random.randint(0, self.size)
            orientation = random.randint(0, 1) == 0 and "V" or "H"
        else:
            #self.pretty_print()
            x = raw_input('What is the x co-ordinate for your ' + str(size) + '? ')
            y = raw_input('What is the y co-ordinate for your ' + str(size) + '? ')
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
            cells[i] = self.composite(x_, y_, 'ship')
        if not self.add_ship(cells):
            self.setup_ship(size, random)
        return True

    def take_cells(self, start_x, start_y, length, direction):
        cells = [None] * length
        for i in range(0, length):
            if direction == "V":
                x = start_x
                y = start_y + i
            elif direction == "H":
                x = start_x + i
                y = start_y
            cells[i] = self.board[(x, y)]
        return cells
        
    def move_ship(self, ship, moving, shift = 1):
        print moving
        if (moving == "left" and ship.cells[0].x == shift - 1 or
                moving == "right" and self.size - ship.cells[-1].x == shift or
                moving == "up" and ship.cells[0].y == shift - 1 or
                moving == "down" and self.size - ship.cells[-1].y == shift):
            return ship
        for i in range(0, ship.length):
            if moving == "left":
                ship.cells[i].x -= shift
            elif moving == "right":
                ship.cells[i].x += shift
            elif moving == "up":
                ship.cells[i].y -= shift
            elif moving == "down":
                ship.cells[i].y += shift
        return ship

    def rotate_ship(self, ship):
        return self.create_ship(
            ship.cells[0].x,
            ship.cells[0].y,
            ship.length,
            ship.get_rotated_direction(),
            ship.cells[0].state,
            True)
    
    def place_ship(self, ship):
        return self.create_ship(
            ship.cells[0].x,
            ship.cells[0].y,
            ship.length,
            ship.direction)
    
    def create_ship(self, start_x, start_y, length, direction, state = 'ship', managed = False):
        ship = None
        
        if managed:
            ship = Ship()
            ship.create(start_x, start_y, length, direction, state)
            ship.cells = [None] * length
            for i in range(0, length):
                x_ = start_x
                y_ = start_y
                if direction == "V":
                    y_ = start_y + i
                elif direction == "H":
                    x_ = start_x + i
                ship.cells[i] = self.composite(x_, y_, state)
        else:
            cells = self.take_cells(start_x, start_y, length, direction)
            if self.add_ship(cells):
                for c in cells:
                    c.state = state
                ship = self.ships[-1]
        
        return ship

    def add_ship(self, cells):
        ship = Ship(cells)
        
        # check collisions
        collision = []
        for new in cells:
            if (new.x < 0 or new.x >= self.size or
                    new.y < 0 or new.y >= self.size):
                #raise OutofboardError()
                return False
            for s in self.ships:
                for full in (s.cells + s.area):
                    if full.x == new.x and full.y == new.y:
                        #collision.append(new)
                        #raise ShipAlreadyThere()
                        return False
        
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
                s += self.get(x, y).draw()
            s += "\n"
        print s
        
    def debug_print(self):
        s = ""
        for y in range(self.size):
            for x in range(self.size):
                ship = self.board[(x, y)].ship
                s += ship == None and "~" or str(ship.length)
            s += "\n"
        print s


class Enemy_Board(Board):

    def __init__(self, size):
        """Init squared field"""
        self.board = {}
        self.ships = []
        self.size = size
        for i in range(self.size):
            for j in range(self.size):
                self.board[(i,j)] = self.composite(i, j, 'fog')

    def add_ship(self, cells):
        ship = Ship(cells)
        
        # check collisions
        collision = []
        for new in cells:
            if (new.x < 0 or new.x >= self.size or
                    new.y < 0 or new.y >= self.size):
                #raise OutofboardError()
                return False
            for s in self.ships:
                for full in (s.cells + s.area):
                    if full.x == new.x and full.y == new.y:
                        #collision.append(new)
                        #raise ShipAlreadyThere()
                        return False
        
        if len(collision) == 0:
            self.ships.append(ship)
            for c in cells:
                self.board[(c.x, c.y)].set_state('fog')
                self.board[(c.x, c.y)].ship = ship
            return True
        return False


