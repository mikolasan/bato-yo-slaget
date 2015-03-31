#!/usr/bin/python
# vim: set fileencoding=utf-8

import os
import sys
import pygame
from pygame.locals import *
from battleship.pygame_game import *


def init_window():
    pygame.init()
    window = pygame.display.set_mode((760, 660))
    pygame.display.set_caption('Tests')


def load_image(name, colorkey=None):
    fullname = os.path.join('art', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def input(events): 
    for event in events: 
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE): 
            sys.exit(0)
        else:
            pass

def draw_background():
    screen = pygame.display.get_surface() # Получаем поверхность, на которой будем рисовать
    background = pygame.Surface(screen.get_size()) # и ее размер
    background = background.convert()
    background.fill((73, 128, 181)) # заполняем цветом
    screen.blit(background, (0, 0)) # рисуем заполненный одним цветом бэкграунд
    #back, back_rect = load_image("back.png") # или загружаем картинку с травой
    #screen.blit(back, (0, 0)) # и рисуем ее
    pygame.display.flip() # переключаем буфер экрана
    return background
    
    
def action(bk):

# test 1
##########
#    ships_list = []
#    screen = pygame.display.get_surface()
#    for i in range(1, 5):
#        boat = PyGame_Cell(i, 1, 'empty')
#        ships_list.append(boat)
#    sprites = pygame.sprite.RenderPlain(ships_list)

# test 2
##########
#    board = PyGame_Board()
#    sprites = board.render

# test 3
##########
#    player = PyGame_Player()
#    settings = [4, 3, 2, 1, 0]
#    player.init_board(10, settings)
#    sprites = player.board.render

    screen = pygame.display.get_surface()
    game = PyGame_Game()
    sprites = pygame.sprite.LayeredUpdates(game.get_sprites())
    
    while 1:
        input(pygame.event.get())
        screen.blit(bk, (0, 0))
        sprites.update() # Стандартный метод проверки, вдруг что-то изменилось. Пригодится для описания движения
        sprites.draw(screen)
        pygame.display.flip()
 
def main():
    init_window()
    bk = draw_background()
    action(bk)


if __name__ == '__main__': main()


