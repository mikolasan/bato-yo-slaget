import pygame
from battleship.ui.font import get_font_path


class Flat(pygame.sprite.Sprite):
    
    font = pygame.font.Font(get_font_path(), 50)
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