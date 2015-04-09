import os
import pygame
from pygame import *
from pygame.locals import *


art_dir = 'art'

gun = pygame.image.load(os.path.join(art_dir, 'aim.bmp'))
gun.set_colorkey((0,0,0))

fonts_dir = 'fonts'
font_name = 'neo_retro.ttf'
font_path = os.path.join(fonts_dir, font_name)
pygame.font.init()


class Aim(pygame.sprite.Sprite):
    x = 0
    y = 0

    sx = 380
    sy = 300
    
    dx = 0
    dy = 0
    
    side = 32
    step = 34
    
    color = (0, 0, 0)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((self.side, self.side))
        self.image = gun
        self.rect = self.image.get_rect()
        self.rect.x = self.sx
        self.rect.y = self.sy

    def update(self):
        self.x = (self.x + self.dx) % 10
        self.rect.x = self.sx + self.x * self.step
        self.dx = 0
        
        self.y = (self.y + self.dy) % 10
        self.rect.y = self.sy + self.y * self.step
        self.dy = 0


class MenuElementFlat(pygame.sprite.Sprite):
    
    font = pygame.font.Font(font_path, 40)
    width = 315
    height = 60
    padding_left = 30
    padding_top = 5
    
    menu_back_c = (212, 227, 230)
    menu_back_selected_c = (116, 213, 218)
    menu_font_c = (0, 0, 0)
    menu_font_selected_c = (0, 0, 0)
    
    def __init__(self, text):
        pygame.sprite.Sprite.__init__(self)
        
        self.is_chosen = False
        
        self.text = text
        self.txt = self.font.render(text ,True, self.menu_font_c)
        
        self._draw()
        self.rect = self.image.get_rect()

    def _draw(self):
        self.image = pygame.Surface((self.width, self.height))
        if self.is_chosen:
            self.image.fill(self.menu_back_selected_c)
            self.image.blit(self.txt, [self.padding_left, self.padding_top])
        else:
            self.image.fill(self.menu_back_c)
            self.image.blit(self.txt, [self.padding_left, self.padding_top])

    def update(self):
        self._draw()
            
        


#gameover = Modal_dialog(315, 100, 'GAME OVER', {'Play again', 'Menu'})
class Modal_dialog(pygame.sprite.LayeredUpdates):
    
    _new = False
    _visible = False
    answer = None
    callback = None
    selection = 0
    
    padding_left = 250
    padding_top = 200
    title_height = 100
    title_c = (241,122,64)
    
    def __init__(self):
        pygame.sprite.LayeredUpdates.__init__(self)
    
    def setup(self):
        self.selection = 0
        self.answer = None
        
        for i, a in enumerate(self._answers):
            item = MenuElementFlat(a)
            if i == self.selection:
                item.is_chosen = True
            item.rect.y = self.padding_top + self.title_height + item.height * i
            item.rect.x = self.padding_left
            self.add(item)

        title = MenuElementFlat(self._title)
        title.menu_back_c = self.title_c
        title.height = self.title_height
        title.rect.y = self.padding_top
        title.rect.x = self.padding_left
        self.add(title)
            
        self._new = False
        self._visible = True


    def select(self, trend):
        self.get_sprite(self.selection).is_chosen = False
        size = len(self._answers)
        if trend == "left":
            self.selection = (self.selection - 1) % size
        elif trend == "right":
            self.selection = (self.selection + 1) % size
        self.get_sprite(self.selection).is_chosen = True

    def choose(self):
        self._visible = False
        self.answer = self.selection
        self.callback(self.answer)
        self.callback = None
    
    def exit(self):
        self._visible = False
        self.callback = None
    
    def get_group(self):
        return self



class Gameover_window(pygame.sprite.Sprite):
    font = pygame.font.Font(os.path.join(fonts_dir, font_name), 70)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((315, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 0

    def update(self, text):
        self.txt1 = self.font.render('GAME OVER' ,True, menu_font_c)
        self.txt2 = self.font.render(text ,True, menu_font_c)
    
        self.rect.y += 2
        self.image.blit(self.txt1, [15,5])
        self.image.blit(self.txt2, [15,50])
        
        
class Menu(object):
    
    def __init__(self):
        self.menu_choice = 0
        self.menu_pick = False
        self.gameover = ''
        
        self.menu_group = sprite.Group()
        
        self.items = ['NEW GAME', 'SETTINGS', 'CONTROLS', 'QUIT']
        for i, a in enumerate(self.items):
            item = MenuElementFlat(a)
            if i == self.menu_choice:
                item.is_chosen = True
            item.rect.y = 200 + 60 * i
            item.rect.x = 250
            setattr(self, 'menu' + str(self.menu_choice + i + 1), item)
            self.menu_group.add(item)
            
    def initialize(self):
        pygame.key.set_repeat() # disable

    def select(self, shift):
        getattr(self, 'menu' + str(self.menu_choice + 1)).is_chosen = False
        
        self.menu_choice += shift
        if self.menu_choice < 0:
            self.menu_choice = 3
        elif self.menu_choice > 3:
            self.menu_choice = 0
            
        getattr(self, 'menu' + str(self.menu_choice + 1)).is_chosen = True
                        
    def get_sprites(self):
        return self.menu_group


