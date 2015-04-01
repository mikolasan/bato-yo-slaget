#!/usr/bin/python
# vim: set fileencoding=utf-8


import random
from Board import Board

class Player(object):
    """The map, ship and firing mechanism for a player of the game battleship.
    """

    def __init__(self, human = False):
        '''Initializes a player's basic requirements'''
        self.human = human
        self.name ='Bot'

    def composite(self, size):
        if self.human:
            return Board(size)
        else:
            return Enemy_Board(size)

    def init_board(self, size, fleet, random = -1):
        self.board = self.composite(size)
        
        human = self.human
        if human:
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


    def set_human(self):
        self.human = True


    def fire(self, board):
        if not self.human:
            #checks to see if the current player should be a computer.
            x = random.randint(0, board.size - 1)
            y = random.randint(0, board.size - 1)
        else:
            x = raw_input('What is the x-coordinate you wish to fire on? ')
            y = raw_input('What is the y-coordinate you wish to fire on? ')
        try:
            x, y = int(x), int(y)
            # verifies that x and y are valid integers.
        except Exception:
            self.fire()
            
        if x >= board.size or y >= board.size:
            #Checks to make sure that x and y and in the scope of the board.
            print 'Out of bounds'
            self.fire()
        elif (board.get(x,y).state == 'miss' or
                board.get(x,y).state == 'fate'):
            #Checks if the current spot has been chosen.
            print 'That coordinate has been fired already'
            self.fire()
            
        return x, y

    def on_fire(self, x, y):
        '''Fired at coordinates (x,y)'''
        cell = self.board.reveal(x,y)
        state = cell.state
        if state == "fate":
            #A player's ship has been hit! Mark it on the board.
            return True
        else:
            #The player has hit and missed.
            return False

    def print_board(self):
        print (self.name + "'s board")
        self.board.pretty_print()

