import os
import pygame


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
        gun = pygame.image.load(os.path.join('assets', 'aim.png'))
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
