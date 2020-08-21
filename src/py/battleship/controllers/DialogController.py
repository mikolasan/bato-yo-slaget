import pygame
from battleship.tim.TimController import TimController as Controller


class DialogController(Controller):
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