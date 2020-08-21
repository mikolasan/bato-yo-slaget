import pygame
from battleship.ui.font import get_font_path


class GameOver(pygame.sprite.Sprite):
    font = pygame.font.Font(get_font_path(), 30)
    menu_font_c = (250, 250, 0)
    
    def __init__(self, text):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((315, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 0
        self.text = text

    def update(self):
        self.txt1 = self.font.render('GAME OVER' ,True, self.menu_font_c)
        self.txt2 = self.font.render(self.text ,True, self.menu_font_c)
    
        self.rect.y += 2
        self.image.blit(self.txt1, [15,5])
        self.image.blit(self.txt2, [15,50])
