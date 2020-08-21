import pygame
from battleship.ui.flat import Flat


class Menu(object):
    
    def __init__(self):
        self.menu_choice = 0
        self.menu_pick = False
        self.gameover = ''
        
        self.menu_group = pygame.sprite.Group()
        
        self.items = ['NEW GAME', 'SETTINGS', 'CONTROLS', 'QUIT']
        for i, a in enumerate(self.items):
            item = Flat(a)
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