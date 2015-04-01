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

class Controller:
    def __init__(self, engine):
        self.engine = engine
    
    def input(self, events):
        for e in events:
            if (e.type == pygame.QUIT) or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE): 
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

class Menu_Controller(Controller):
    def input(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.menu_choice -= 1
                    if self.menu_choice < 0:
                        self.menu_choice = 0

                elif e.key == pygame.K_DOWN:
                    self.menu_choice += 1
                    if self.menu_choice > 3:
                        self.menu_choice = 3

                elif e.key == pygame.K_RETURN:
                    self.menu_pick = True
                    if self.menu_choice == 3 and self.menu_pick:
                        return True
                    
                elif e.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
                    self.menu_choice = 0

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RETURN:
                    self.menu_pick = False
                    
        return False
        
class Game_Controller(Controller):
    def input(self, events):
        for e in events:
            if e.type == pygame.QUIT: 
                return True

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.ys = -35

                elif e.key == pygame.K_DOWN:
                    self.ys = 35

                elif e.key == pygame.K_LEFT:
                    self.xs = -35

                elif e.key == pygame.K_RIGHT:
                    self.xs = 35

                elif e.key == pygame.K_SPACE:
                    
                    self.set_ship -= 1
                    ship_coord_check(self.descartes_p, self.all_sprites,self. pla_board, self.set_ship)
                    
                elif e.key == pygame.K_RETURN:
                    if self.cpu_player > 0:
                        self.res_p = res_check(self.descartes_cpu, self.aim, self.cpu_board)
                        
                        hit_coord_check(self.descartes_cpu, self.aim, self.cpu_board)
                        self.cpu_player = (-1)*self.cpu_player

                elif e.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
                    self.menu_choice = 0

                elif e.key == pygame.K_w:
                    self.set_ship += 1

                elif e.key == pygame.K_TAB:
                    # rotate ship
                    pass

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    self.ys = 0
                if e.key == pygame.K_LEFT:
                    self.xs=0

                elif e.key == pygame.K_RIGHT:
                    self.xs = 0

                elif e.key == pygame.K_DOWN:
                    self.ys = 0
                    
        return False
        
        
    def handle_pygame_event(self,e):
        """Ideally, build this out with state so that the world
        can make a query like controller.enter_was_pressed or key_held_for(3)"""
