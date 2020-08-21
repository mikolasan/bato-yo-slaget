#!/usr/bin/python
# vim: set fileencoding=utf-8

import os
import sys
import pygame
from pygame.locals import *
from battleship.pygame_engine import *
from battleship.pygame_game import *
from battleship.pygame_controller import *


def init_window():
    pygame.init()
    window = pygame.display.set_mode((760, 660))
    pygame.display.set_caption('Tests')
    pygame.display.set_icon(pygame.image.load(os.path.join("art", "icons", "ico.png")))

    
def action(bk):

# test 1
##########
#    ships_list = []
#    screen = pygame.display.get_surface()
#    for i in range(1, 5):
#        boat = PyCell(i, 1, 'empty')
#        ships_list.append(boat)
#    sprites = pygame.sprite.RenderPlain(ships_list)

# test 2
##########
#    board = PyBoard()
#    sprites = board.render

# test 3
##########
#    player = PyPlayer()
#    settings = [4, 3, 2, 1, 0]
#    player.init_board(10, settings)
#    sprites = player.board.render

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
    
    init_window()
    back = draw_background()
    action(bk)


if __name__ == '__main__': main()


