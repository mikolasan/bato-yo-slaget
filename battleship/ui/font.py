import os
import pygame

font_path = os.path.join('assets', 'fonts', 'Westmeath.ttf')
pygame.font.init()


def get_font_path():
    return font_path
