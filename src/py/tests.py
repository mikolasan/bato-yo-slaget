#!/usr/bin/python
# vim: set fileencoding=utf-8

from battleship.Cell import Cell
from battleship.Ship import Ship
from battleship.Board import Board
from battleship.Player import Player

def test_cells():
    board = []
    for i in range(1,10):
        board.append(Cell(0, i))
    for c in board:
        print c.x, c.y, c.state


def test_ship():
    ship = Ship()
    ship.create(0, 0, 3, "V")
    print ship.name, " area: ", len(ship.area)
    for c in ship.area:
        print c.x, c.y


def test_board():
    board = Board(10)
    ship1 = Ship()
    ship1.create(0, 0, 3, "V")
    ship2 = Ship()
    ship2.create(0, 0, 3, "H")
    board.add_ship(ship1.cells)
    board.add_ship(ship2.cells)
    board.pretty_print()


def test_player():
    player = Player()
    settings = [4, 3, 2, 1, 0]
    player.init_board(10, settings)
    player.board.pretty_print()
    x, y = player.fire(player.board)
    print x, y
    player.on_fire(x, y)
    player.board.pretty_print()


test_cells()
test_ship()
test_board()    
test_player()


