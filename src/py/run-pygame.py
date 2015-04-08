#!/usr/bin/python
# vim: set fileencoding=utf-8

from battleship.pygame_engine import *
from battleship.pygame_game import *
from battleship.pygame_controller import *
from battleship.pygame_elements import *
 
def main():
    engine = Engine()
    engine.name = 'Bato-yo-slaget'
    engine.start()
    
    game = PyGame_Game()
    game_controller = Game_Controller(engine)
    engine.add_scene('battleship', game, game_controller)

    menu = Menu()
    menu_controller = Menu_Controller(engine)
    engine.add_scene('menu', menu, menu_controller)
    
    clock = pygame.time.Clock()
    while 1:
        engine.draw_scene()
        clock.tick(20)

if __name__ == '__main__': main()


