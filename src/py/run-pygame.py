#!/usr/bin/python
# vim: set fileencoding=utf-8

import pygame
from battleship.tim.TimEngine import TimEngine as Engine
from battleship.PyPlay import PyPlay
from battleship.controllers.GameController import GameController
from battleship.controllers.MenuController import MenuController
from battleship.ui.menu import Menu


def main():
    engine = Engine()
    engine.name = 'Bato yo slaget'
    engine.start()
    
    game = PyPlay()
    game_controller = GameController(engine)
    engine.add_scene('battleship', game, game_controller)

    menu = Menu()
    menu_controller = MenuController(engine)
    engine.add_scene('menu', menu, menu_controller)
    
    clock = pygame.time.Clock()
    while 1:
        engine.draw_scene()
        clock.tick(20)


if __name__ == '__main__':
    main()


