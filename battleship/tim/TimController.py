#
# controller.py
# not well implemented for expansion
# but, provides a lot of nice base behavior:
# * alt-enter to toggle fullscreen
# * minimise pauses the engine (although the world still needs to check if the engine is paused)
# * un minimise unpauses the engine
# * can resize the window to change the display resolution
# * can quit the game

import sys
import pygame


class TimController:
    def __init__(self, engine):
        self.engine = engine

    def input(self, events):
        for e in events:
            if (e.type == pygame.QUIT) or (e.type == pygame.KEYDOWN
                                           and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit(0)


#    def input(self):
#        engine = self.engine
#        pygame.event.pump()
#        for e in events:
#            if e.type==pygame.ACTIVEEVENT:
#                if e.gain==0 and (e.state==6 or e.state==2 or e.state==4):
#                    self.engine.pause()
#                    continue
#                if e.gain==1 and (e.state==6 or e.state==2 or e.state==4):
#                    self.engine.unpause()
#                    continue
#            if e.type==pygame.VIDEORESIZE:
#                w,h = e.w,e.h
#                engine.swidth = w
#                engine.sheight = h
#                engine.make_screen()
#                continue
#            if e.type == pygame.QUIT:
#                self.engine.stop()
#                continue
#            if e.type==pygame.KEYDOWN and\
#            e.key==pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
#                engine.fullscreen = 1-engine.fullscreen
#                engine.make_screen()
#                continue
#            self.handle_pygame_event(e)
#        if engine.world:
#            engine.world.input(self)
