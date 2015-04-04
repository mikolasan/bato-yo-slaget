#!/usr/bin/python
# vim: set fileencoding=utf-8

#
# engine.py - handles generally running the game
# can set a game resolution (iwidth, iheight) as well as a screen resolution
# the screen scales to fit
# also has a builting framerate counter
#

import os
import pygame
from pygame.locals import *
from battleship.pygame_game import *
from battleship.pygame_controller import *

def fit(surf,size):
    surf = pygame.transform.scale(surf,size)
    return surf

class Engine:
    
    def __init__(self):
        self.fullscreen = False
        #The screen width, what resolution the screen is scaled to
        self.swidth = 760
        self.sheight = 660
        #The interactive width, what resolution the game is actually rendered at
        self.iwidth = 320
        self.iheight = 240
        self.window = None   #The window is the actual window
        self.surface = None   #The surface is what will be displayed, most of the time draw to this
        self.blank = None
        self.back = None
        self.running = False   #If this is set to false, the game will quit
        self.paused = False   #Not implemented, should be controlled by the world
        self.framerate = 60    #What framerate the game runs at
        self.dt = 0
        self.show_fps = True
        self.clock = None
        self.world = None   #Change what world is set to to change between scenes or modes
        self.scenes = {}
        self.next_tick = 0.0
    
    def start(self):
        """Separate from __init__ in case we want to make the object before making the screen"""
        pygame.init()
        self.make_screen()
        self.back = self.draw_background()
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(os.path.join("fonts", "neo_retro.ttf"),12)
    
    def stop(self):
        self.running = False
    
    def pause(self):
        self.paused = True
    
    def unpause(self):
        self.paused = False
    
    def update(self):
        """One tick, according to dt"""
        self.next_tick += self.dt
        if self.world:
            while self.next_tick>0:
                self.next_tick -= 1
                self.world.update()
    
    def load_image(self, name, colorkey=None):
        fullname = os.path.join('art', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print "Cannot load image:", name
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()


    def draw_background(self):
        screen = pygame.display.get_surface() # Получаем поверхность, на которой будем рисовать
        background = pygame.Surface(screen.get_size()) # и ее размер
        background = background.convert()
        # заполняем цветом
        background.fill((73, 128, 181)) 
        screen.blit(background, (0, 0)) # рисуем заполненный одним цветом бэкграунд
        # или загружаем картинку
        #back, back_rect = load_image("back.png") 
        #screen.blit(back, (0, 0)) # и рисуем ее
        
        #pygame.display.flip() # переключаем буфер экрана
        return background
        
    def make_screen(self):
        flags = pygame.RESIZABLE|pygame.FULLSCREEN*self.fullscreen
        self.window = pygame.display.set_mode([self.swidth,self.sheight],flags)
        self.surface = pygame.display.get_surface() #pygame.Surface([self.iwidth,self.iheight]).convert()
        #self.blank = self.surface.convert()
        #self.blank.fill([0,0,0])
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(pygame.image.load(os.path.join("art", "icons", "ico.png")))
            
    
    def clear_screen(self):
        self.surface.blit(self.blank,[0,0])
    
    def add_scene(self, name, obj, ctrl, set_current = True):
        self.scenes[name] = dict({'world': obj, 'controller': ctrl})
        if set_current:
            self.scene = name
            self.world = obj
            self.controller = ctrl
            
    def switch_scene(self, name):
        if name in self.scenes:
            self.scene = name
            self.world = self.scenes[name]['world']
            self.controller = self.scenes[name]['controller']
    
    def draw_scene(self):
    
        self.controller.input(pygame.event.get())
        
        screen = self.surface
        screen.blit(self.back, (0, 0))
        
        sprites = pygame.sprite.LayeredUpdates(self.world.get_sprites())
        sprites.update() # Стандартный метод проверки, вдруг что-то изменилось. Пригодится для описания движения
        sprites.draw(screen)
        
        pygame.display.flip()

        
