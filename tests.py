#!/usr/bin/python
# vim: set fileencoding=utf-8

from battleship import Cell

def test_cells():
    board = []
    for i in range(1,10):
        board.append(Cell(0, i))
    for c in board:
        print c.x, c.y, c.state
        
#test_cells()


from battleship import Ship

def test_ship():
    ship = Ship()
    ship.create(0, 0, 3, "V")
    print ship.name, " area: ", len(ship.area)
    for c in ship.area:
        print c.x, c.y
    
        
#test_ship()


from battleship import Board

def test_board():
    board = Board(10)
    ship1 = Ship()
    ship1.create(0, 0, 3, "V")
    ship2 = Ship()
    ship2.create(0, 0, 3, "H")
    board.add_ship(ship1.cells)
    board.add_ship(ship2.cells)
    board.pretty_print()
    
        
#test_board()

from battleship import Player

def test_player():
    player = Player()
    settings = [4, 3, 2, 1, 0]
    player.init_board(10, settings)
    player.board.pretty_print()
    #player.turn()
    
test_player()
    
