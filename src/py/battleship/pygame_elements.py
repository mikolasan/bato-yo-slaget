import pygame
import os

art_dir = 'art'
fonts_dir = 'fonts'
gun = pygame.image.load(os.path.join(art_dir, 'aim.bmp'))
gun.set_colorkey((0,0,0))


pygame.font.init()


class Aim(pygame.sprite.Sprite):
    x = 21
    y = 21

    x_shift = 0
    y_shift = 0
    
    color = (0, 0, 0)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))

        self.image = gun
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x += self.x_shift
        self.rect.y += self.y_shift
        
        



class MenuElement(pygame.sprite.Sprite):
    c = (250,250,250)
    
    font = pygame.font.Font(os.path.join(fonts_dir,'vera.ttf'), 20)
    font_big = pygame.font.Font(os.path.join(fonts_dir, 'vera.ttf'), 30)
    
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
            self.txt = self.font_big.render(self.text ,True, (5,25,245))
            self.image.fill((245,237,5))
            self.image.blit(self.txt, [-5,5])

        if not self.is_chosen:
            self.txt = self.font.render(self.text ,True, (0,0,0))
            self.image.fill((5,25,245))
            self.image.blit(self.txt, [5,5])
            
        self.image.set_colorkey((0,0,0))
        


class MainMenuElement(pygame.sprite.Sprite):
    c = (250,250,250)
    
    font = pygame.font.Font(os.path.join(fonts_dir, 'vera.ttf'), 40)
    font_big = pygame.font.Font(os.path.join(fonts_dir, 'vera.ttf'), 50)
    
    def __init__(self, text, y, is_chosen):
        pygame.sprite.Sprite.__init__(self)
        
        self.txt = self.font.render(text ,True, (212,227,52))
        self.text = text
        self.is_chosen = is_chosen

        self.image = pygame.Surface((315, 100))
        
            
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image.blit(self.txt, [20,5])
        self.rect.x = 250
        self.rect.y = y

        

    def update(self):
        self.image = pygame.Surface((315, 60))
        
        if self.is_chosen:
            self.image.fill((5,25,245))
            self.txt = self.font_big.render(self.text ,True, (245,237,5))
            self.image.blit(self.txt, [15,5])

        if not self.is_chosen:
            self.image.fill((5,25,245))
            self.txt = self.font.render(self.text ,True, (212,227,52))
            self.image.blit(self.txt, [50,5])
            
        self.image.set_colorkey((0,0,0))


class Gameover_window(pygame.sprite.Sprite):
    font = pygame.font.Font(os.path.join(fonts_dir, 'vera.ttf'), 70)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((315, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 0

    def update(self, text):
        self.txt1 = self.font.render('GAME OVER' ,True, (212,227,52))
        self.txt2 = self.font.render(text ,True, (212,227,52))
    
        self.rect.y += 2
        self.image.blit(self.txt1, [15,5])
        self.image.blit(self.txt2, [15,50])
