import pygame
from battleship.ui.flat import Flat


#gameover = Popup(315, 100, 'GAME OVER', {'Play again', 'Menu'})
class Popup(pygame.sprite.LayeredUpdates):

    _new = False
    _visible = False
    answer = None
    callback = None
    selection = 0

    padding_left = 250
    padding_top = 200
    title_height = 100
    title_c = (241, 122, 64)

    def __init__(self):
        pygame.sprite.LayeredUpdates.__init__(self)

    def setup(self):
        self.selection = 0
        self.answer = None

        for i, a in enumerate(self._answers):
            item = Flat(a)
            if i == self.selection:
                item.is_chosen = True
            item.rect.y = self.padding_top + self.title_height + item.height * i
            item.rect.x = self.padding_left
            self.add(item)

        title = Flat(self._title)
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
        if self.callback and callable(self.callback):
            self.callback(self.answer)
        self.callback = None

    def exit(self):
        self._visible = False
        self.callback = None

    def get_group(self):
        return self
