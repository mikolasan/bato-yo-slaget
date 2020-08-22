import pygame
from battleship.ui.colors import Colors
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
            item.rect.y = 200 + item.height * i
            item.rect.x = 250
            setattr(self, 'menu' + str(self.menu_choice + i + 1), item)
            self.menu_group.add(item)
        self.title = Flat('BATO YO SLAGET')
        self.title.menu_back_c = (241, 80, 37)
        # self.title.menu_font_c = Colors.flat_back
        self.title.menu_font_c = Colors.font_selected
        self.title.render_text()
        self.title.width = 400
        self.title.height = 70
        self.title.rect.x = 200
        self.title.rect.y = 60
        self.menu_group.add(self.title)

    def initialize(self):
        pygame.key.set_repeat()  # disable

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