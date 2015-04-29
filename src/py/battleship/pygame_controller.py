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

class Modal_Controller(Controller):
    def input(self, events):
        
        dialog = self.engine.dialog
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    dialog.exit()
                    
                elif e.key == pygame.K_UP:
                    dialog.select('left')

                elif e.key == pygame.K_DOWN:
                    dialog.select('right')
                       
                elif e.key == pygame.K_RETURN:
                    dialog.choose()
                    

class Menu_Controller(Controller):
    def input(self, events):
        
        Controller.input(self, events)
        
        scene = self.engine.world
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    scene.select(-1)
                    
                elif e.key == pygame.K_DOWN:
                    scene.select(1)

                elif e.key == pygame.K_RETURN:
                    if scene.menu_choice == 0:
                        self.engine.switch_scene('battleship')
                        self.engine.world.start()
                    elif scene.menu_choice == 3:
                        sys.exit(0)
                    
#                elif e.key == pygame.K_ESCAPE:
#                    self.pause = not self.pause
#                    scene.menu_choice = 0

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RETURN:
                    scene.menu_pick = False

        
class Game_Controller(Controller):
    def input(self, events):
    
        Controller.input(self, events)
        
        scene = self.engine.world
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                direction = None
                
                if e.key == pygame.K_UP:
                    direction = 'up'

                elif e.key == pygame.K_DOWN:
                    direction = 'down'

                elif e.key == pygame.K_LEFT:
                    direction = 'left'

                elif e.key == pygame.K_RIGHT:
                    direction = 'right'

                elif e.key == pygame.K_SPACE:
                    if scene.curr_player.stage == "planning":
                        scene.place_ship()
                    
                elif e.key == pygame.K_RETURN:
                    if scene.curr_player.stage == "scanning":
                        scene.hit()

                elif e.key == pygame.K_ESCAPE:
                    self.engine.switch_scene('menu')

                elif e.key == pygame.K_TAB:
                    if scene.curr_player.stage == "planning":
                        scene.rotate_ship()
                
                if direction:
                    if scene.curr_player.stage == "planning":
                        scene.move_ship(direction)
                    elif scene.curr_player.stage == "scanning":
                        scene.move_aim(direction)

