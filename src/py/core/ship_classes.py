import pygame
import os

art_dir = 'art'
fonts_dir = 'fonts'
gun = pygame.image.load(os.path.join(art_dir, 'aim.bmp'))
gun.set_colorkey((0,0,0))


pygame.font.init()

class Ship(pygame.sprite.Sprite):
    x = 391
    y = 291

    x_shift = 0
    y_shift = 0


    

    color = ((200,0,0))
    def __init__(self, w, h):
        self.w = w
        self.h = h
        rotate = 0

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()


        
    def update(self):
        self.rect.x += self.x_shift
        self.rect.y += self.y_shift

    def rotate(self):
        self.w, self.h = self.h, self.w
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)
        
        
        
        


class Cell(pygame.sprite.Sprite):
    x = 0
    y = 0

    color1 = (98, 238,154)
    color2 = (24, 216,235)
    color3 = (250,250,250)
    color4 = (15,25,71)
    def __init__(self, typ):
        self.typ = typ
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        if self.typ == 'p':
            self.image.fill(self.color1)
        elif self.typ == 'c':
            self.image.fill(self.color2)
        elif self.typ == 'd' or self.typ == 'o':
            self.image.fill(self.color3)
        elif self.typ == 'g':
            self.image.fill(self.color4)
        elif self.typ == 'dead':
            self.image.fill((0,0,0))
        elif self.typ == 'damaged':
            self.image.fill((50,50,50))
            
            
            
        self.rect = self.image.get_rect()
    
    def update(self):
        if self.typ == 'p':
            self.image.fill(self.color1)
        elif self.typ == 'c':
            self.image.fill(self.color2)
        elif self.typ == 'd' or self.typ == 'o':
            self.image.fill(self.color3)
        elif self.typ == 'g':
            self.image.fill(self.color4)
        elif self.typ == 'dead':
            self.image.fill((0,0,0))
        elif self.typ == 'damaged':
            self.image.fill((50,50,50))
        
        


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


        

    
        
            
        
        
        
        
        
        

    

    
    
    
        
        

    
    

