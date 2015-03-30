#!/usr/bin/python
# vim: set fileencoding=utf-8

import os
import sys
import pygame
from pygame.locals import *
from battleship.Cell import Cell


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


class PyGame_Cell(Cell, pygame.sprite.Sprite):

	 # {'fog','empty', 'ship', 'miss', 'near', 'fate'}
    
    player_c = (15,25,71) # dark blue
    empty_c = (24, 216,235) # blue
    near_c = (98, 238,154) # green
    fate_c = (250,250,250) # black

    size = 32

    def __init__(self, x, y, state):
        Cell.__init__(self, x, y, state)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.size, self.size))
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.left = self.size * self.x
        self.rect.top = self.size * self.y

    def update(self):
        self.draw()    
    
    def draw(self):
        if self.state == 'ship':
            self.image.fill(self.player_c)
        elif self.state == 'empty':
            self.image.fill(self.empty_c)
        elif self.state == 'near':
            self.image.fill(self.near_c)
        elif self.state == 'fate':
            self.image.fill(self.fate_c)
            
    
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
    background.fill((0, 0, 0)) # заполняем цветом
    screen.blit(background, (0, 0)) # рисуем заполненный одним цветом бэкграунд
    back, back_rect = load_image("back.png") # или загружаем картинку с травой
    screen.blit(back, (0, 0)) # и рисуем ее
    pygame.display.flip() # переключаем буфер экрана
    return back
    
    
def action(bk):
    ships_list = [] # Список со всем животными. Пригодится, если будем добавлять новых
    screen = pygame.display.get_surface()
    boat = PyGame_Cell(2, 1, 'empty') # Помещаем слона по координатам х=10, у=10
    ships_list.append(boat)
    fleet = pygame.sprite.RenderPlain((boat)) # Засовываем всех наших животных в класс RenderPlain для отображения спрайтов на экране
 
    while 1:
        input(pygame.event.get())
        screen.blit(bk, (0, 0))
        fleet.update() # Стандартный метод проверки, вдруг что-то изменилось. Пригодится для описания движения
        fleet.draw(screen)
        pygame.display.flip()
 
def main():
    init_window()
    bk = draw_background()
    action(bk)


if __name__ == '__main__': main()


