import pygame
from battleship.ui.colors import Colors
from battleship.ui.font import get_font_path


class Flat(pygame.sprite.Sprite):

    font = pygame.font.Font(get_font_path(), 50)
    width = 315
    height = 70
    padding_left = 30
    padding_top = 5

    menu_back_c = Colors.flat_back
    menu_back_selected_c = Colors.flat_back_selected
    menu_font_c = Colors.font
    menu_font_selected_c = Colors.font_selected

    def __init__(self, text):
        pygame.sprite.Sprite.__init__(self)

        self.is_chosen = False

        self.text = text
        self.render_text()
        self._draw()
        self.rect = self.image.get_rect()

    def render_text(self):
        self.txt = self.font.render(self.text, True, self.menu_font_c)
        self.txt_sel = self.font.render(self.text, True,
                                        self.menu_font_selected_c)

    def _draw(self):
        self.image = pygame.Surface((self.width, self.height))
        if self.is_chosen:
            self.image.fill(self.menu_back_selected_c)
            self.image.blit(self.txt_sel,
                            [self.padding_left, self.padding_top])
        else:
            self.image.fill(self.menu_back_c)
            self.image.blit(self.txt, [self.padding_left, self.padding_top])

    def update(self):
        self._draw()