#!/usr/bin/python
# vim: set fileencoding=utf-8

import os
import sys
import pygame
from pygame.locals import *
from battleship.pygame_engine import *
from battleship.pygame_game import *
from battleship.pygame_controller import *



    
def action(bk):

    screen = pygame.display.get_surface()
    game = PyGame_Game()
    sprites = pygame.sprite.LayeredUpdates(game.get_sprites())

    controller = Controller(game)

    while 1:
        controller.input(pygame.event.get())
        
        screen.blit(bk, (0, 0))
        sprites.update() # Стандартный метод проверки, вдруг что-то изменилось. Пригодится для описания движения
        sprites.draw(screen)
        pygame.display.flip()
 
def main():
    engine = Engine()
    engine.name = 'Bato-yo-slaget'
    engine.start()
    


if __name__ == '__main__': main()


