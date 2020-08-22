import pygame
import sys
from battleship.tim.TimController import TimController as Controller


class MenuController(Controller):
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