import os
import pygame
from pygame import *
from pygame.locals import *


art_dir = 'art'

gun = pygame.image.load(os.path.join(art_dir, 'aim.bmp'))
gun.set_colorkey((0,0,0))

fonts_dir = 'fonts'
font_name = 'neo_retro.ttf'
menu_back_c = (212, 227, 230)
menu_back_selected_c = (116, 213, 218)
menu_font_c = (0, 0, 0)
menu_font_selected_c = (0, 0, 0)


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
        
        
class MenuElement(pygame.sprite.Sprite):
    c = (250,250,250)
    
    font = pygame.font.Font(os.path.join(fonts_dir,font_name), 20)
    font_big = pygame.font.Font(os.path.join(fonts_dir, font_name), 30)
    
    def __init__(self, text, y, is_chosen):
        pygame.sprite.Sprite.__init__(self)
        
        self.txt = self.font.render(text ,True, (100,100,100))
        self.text = text
        self.is_chosen = is_chosen

        self.image = pygame.Surface((200, 60))
            
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image.blit(self.txt, [5,5])
        self.rect.x = 320
        self.rect.y = y

        

    def update(self):
        self.image = pygame.Surface((200, 60))
        
        if self.is_chosen:
            self.txt = self.font_big.render(self.text ,True, menu_back_c)
            self.image.fill(menu_font_selected_c)
            self.image.blit(self.txt, [-5,5])

        if not self.is_chosen:
            self.txt = self.font.render(self.text ,True, (0,0,0))
            self.image.fill(menu_back_c)
            self.image.blit(self.txt, [5,5])
            
        self.image.set_colorkey((0,0,0))
        


class MainMenuElement(pygame.sprite.Sprite):
    
    font = pygame.font.Font(os.path.join(fonts_dir, font_name), 40)
    font_big = pygame.font.Font(os.path.join(fonts_dir, font_name), 50)
    
    def __init__(self, text, y, is_chosen):
        pygame.sprite.Sprite.__init__(self)
        
        self.txt = self.font.render(text ,True, menu_font_c)
        self.text = text
        self.is_chosen = is_chosen

        self.image = pygame.Surface((315, 100))
        
            
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image.blit(self.txt, [30,5])
        self.rect.x = 250
        self.rect.y = y

        

    def update(self):
        self.image = pygame.Surface((315, 60))
        
        if self.is_chosen:
            self.image.fill(menu_back_selected_c)
            self.txt = self.font.render(self.text ,True, menu_font_selected_c)
            #self.txt = self.font_big.render(self.text ,True, menu_font_selected_c)
            self.image.blit(self.txt, [30,5])

        if not self.is_chosen:
            self.image.fill(menu_back_c)
            self.txt = self.font.render(self.text ,True, menu_font_c)
            self.image.blit(self.txt, [30,5])
            
        self.image.set_colorkey((0,0,0))


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
        self.menu_group = sprite.Group()
        
        self.menu1 = MenuElement('CONTINUE', 200, True)
        self.menu_group.add(self.menu1)
        
        self.menu2 = MenuElement('SETTINGS', 260, False)
        self.menu_group.add(self.menu2)

        self.menu3 = MenuElement('CONTROLS', 320, False)
        self.menu_group.add(self.menu3)

        self.menu4 = MenuElement('QUIT', 380, False)
        self.menu_group.add(self.menu4)
        
        self.main_menu_group = sprite.Group()
        
        self.mmenu1 = MainMenuElement('NEW GAME', 200, True)
        self.main_menu_group.add(self.mmenu1)
        
        self.mmenu2 = MainMenuElement('SETTINGS', 260, False)
        self.main_menu_group.add(self.mmenu2)

        self.mmenu3 = MainMenuElement('CONTROLS', 320, False)
        self.main_menu_group.add(self.mmenu3)

        self.mmenu4 = MainMenuElement('QUIT', 380, False)
        self.main_menu_group.add(self.mmenu4)
        
        self.gameover_group = sprite.Group()
        
        self.gameover_window = Gameover_window()
        self.gameover_group.add(self.gameover_window)
        
        self.menu_choice = 0
        self.menu_pick = False
        self.gameover = ''

    def initialize(self):
        pygame.key.set_repeat() # disable

    def select(self, shift):
        getattr(self, 'mmenu' + str(self.menu_choice + 1)).is_chosen = False
        
        self.menu_choice += shift
        if self.menu_choice < 0:
            self.menu_choice = 3
        elif self.menu_choice > 3:
            self.menu_choice = 0
            
        getattr(self, 'mmenu' + str(self.menu_choice + 1)).is_chosen = True
                        
    def get_sprites(self):
        return self.main_menu_group


