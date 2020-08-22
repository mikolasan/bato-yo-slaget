import pygame
from battleship.tim.TimController import TimController as Controller


class GameController(Controller):
    def input(self, events):
        super().input(self, events)
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

                elif e.key == pygame.K_RETURN:
                    if scene.curr_player.stage == "planning":
                        scene.place_ship()
                    elif scene.curr_player.stage == "scanning":
                        scene.hit()

                elif e.key == pygame.K_ESCAPE:
                    self.engine.switch_scene('menu')

                elif e.key == pygame.K_SPACE:
                    if scene.curr_player.stage == "planning":
                        scene.rotate_ship()

                if direction:
                    if scene.curr_player.stage == "planning":
                        scene.move_ship(direction)
                    elif scene.curr_player.stage == "scanning":
                        scene.move_aim(direction)
