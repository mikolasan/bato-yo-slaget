#!/usr/bin/python
# vim: set fileencoding=utf-8


# http://stackoverflow.com/questions/2150108/efficient-way-to-shift-a-list-in-python
from collections import deque
from Player import Player

 
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

        self.players = deque()
        for i in range(0, 2):
            p = Player()
            if n_players > i:
                p.set_human()
                p.name = raw_input('What is your name player ' + str(i+1) + '? ')
            p.init_board(size, fleet_settings)
            self.players.append(p)
            

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
        
    def clear_screen(self):
        for n in range(40):
            print ''

    def turn(self):
        x, y = self.curr_player.fire(self.curr_opponent.board)
        hit = self.curr_opponent.on_fire(x, y)
        self.curr_opponent.print_board()
        self.game_over = (len(self.curr_opponent.board.ships) == 0)
        
        if not hit:
            #Swap player's seats.
            self.players.rotate(1)
            self.curr_player = self.players[0]
            self.curr_opponent = self.players[1]
      

    def play(self):
        while not self.game_over:
            self.turn()
        print self.curr_opponent.name + ''' wins!'''


