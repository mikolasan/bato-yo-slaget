#!/usr/bin/python
# vim: set fileencoding=utf-8

import os
import pygame
from battleship.controllers.DialogController import DialogController
from battleship.ui.colors import Colors
from battleship.ui.font import get_font_path
from battleship.ui.popup import Popup


class TimEngine:
    """Engine generally running the game
    can set a game resolution (iwidth, iheight) as well as a screen resolution
    the screen scales to fit
    also has a builting framerate counter"""
    def __init__(self):
        self.name = "Untitled"
        self.fullscreen = False
        # The screen width, what resolution the screen is scaled to
        self.swidth = 760
        self.sheight = 660
        # The interactive width, what resolution the game is actually rendered at
        self.iwidth = 320
        self.iheight = 240
        self.window = None  # The window is the actual window
        self.surface = None  # The surface is what will be displayed, most of the time draw to this
        self.blank = None
        self.back = None
        self.back_color = Colors.background
        self.running = False  # If this is set to false, the game will quit
        self.paused = False  # Not implemented, should be controlled by the world
        self.framerate = 60  # What framerate the game runs at
        self.dt = 0
        self.show_fps = True
        self.clock = None
        self.world = None  # Change what world is set to to change between scenes or modes
        self.dialog = Popup()
        self.dialog.controller = DialogController(self)
        print("create instance of Popup", self.dialog._new)
        self.scenes = {}
        self.next_tick = 0.0

    def start(self):
        """Separate from __init__ in case we want to make the object before making the screen"""
        pygame.init()
        self.make_screen()
        self.back = self.draw_background()
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(get_font_path(), 12)

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
            while self.next_tick > 0:
                self.next_tick -= 1
                self.world.update()

    @staticmethod
    def load_image(name, colorkey=None):
        fullname = os.path.join('assets', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print("Cannot load image:", name)
            raise SystemExit(message)
        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect()

    def draw_background(self):
        # Получаем поверхность, на которой будем рисовать
        screen = pygame.display.get_surface()
        background = pygame.Surface(screen.get_size())  # и ее размер
        background = background.convert()
        # заполняем цветом
        background.fill(self.back_color)
        screen.blit(background, (0, 0))
        # или загружаем картинку
        # back, back_rect = load_image("back.png")
        # screen.blit(back, (0, 0)) # и рисуем ее

        # pygame.display.flip() # переключаем буфер экрана
        return background

    def make_screen(self):
        flags = pygame.RESIZABLE | pygame.FULLSCREEN * self.fullscreen
        self.window = pygame.display.set_mode([self.swidth, self.sheight],
                                              flags)
        self.surface = pygame.display.get_surface()
        # pygame.Surface([self.iwidth,self.iheight]).convert()
        # print('screen', self.surface.get_bitsize())

        # self.blank = self.surface.convert()
        # self.blank.fill([0,0,0])
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(
            pygame.image.load(os.path.join("assets", "icon.png")))

    def clear_screen(self):
        self.surface.blit(self.blank, [0, 0])

    def add_scene(self, name, obj, ctrl, set_current=True):
        self.scenes[name] = dict({'world': obj, 'controller': ctrl})
        if set_current:
            self.switch_scene(name)

    def switch_scene(self, name):
        if name in self.scenes:
            self.scene = name
            self.world = self.scenes[name]['world']
            self.controller = self.scenes[name]['controller']
            if self.world.initialize:
                self.world.initialize()

    def draw_scene(self):
        if not self.dialog._visible:
            self.controller.input(pygame.event.get())

        screen = self.surface
        screen.blit(self.back, (0, 0))

        if self.world.get_sprites:
            sprites = pygame.sprite.LayeredUpdates(self.world.get_sprites())
            sprites.update()
            sprites.draw(screen)
        elif self.world.get_group:
            sprites = self.world.get_group()
            sprites.update()
            sprites.draw(screen)

        if self.dialog._new:
            self.dialog.setup()
        if self.dialog._visible:
            self.dialog.controller.input(pygame.event.get())
            self.dialog.update()
            self.dialog.draw(screen)

        pygame.display.flip()
