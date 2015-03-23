
import os
import random
import pygame
from pygame import *
from game_functions import *
from ship_classes import *


background_image = pygame.image.load(os.path.join(art_dir, 'back.bmp'))
menu_image = pygame.image.load(os.path.join(art_dir, 'menu.bmp'))

back_color = (15,25,71)
s_color = (236, 245, 154)


class Game():
    pause = False
    all_sprites = None
    p_cells = None
    cpu_cells = None
    aim_group= None

    main_menu_group = None
    menu_group = None
    gameover_group = None

    cpu_player = 0

    set_ship = 10
    xs = 0
    ys = 0

    res = ''
    res_p = ''
    descartes_p = []
    descartes_cpu = []

    window = 'main'
    menu_choice = 0
    menu_pick = False
    gameover = ''

    
    def __init__(self):
        self.player_screen = Surface((350, 350))
        self.cpu_screen = Surface((350, 350))

        self.all_sprites = pygame.sprite.Group()
        self.p_cells = sprite.Group()
        self.cpu_cells = sprite.Group()
        self.dam_cells = sprite.Group()
        self.ship_sprites = sprite.Group()
        self.aim_group = sprite.Group()
        self.menu_group = sprite.Group()
        self.main_menu_group = sprite.Group()
        self.gameover_group = sprite.Group()
        

        self.ship4 = Ship(137,32)
        self.all_sprites.add(self.ship4)
        self.ship_sprites.add(self.ship4)
        self.ship4.rect.x = 391
        self.ship4.rect.y = 291

        self.ship3_1 = Ship(102,32)
        self.ship3_1.rect.x = 391
        self.ship3_1.rect.y = 291
        self.ship_sprites.add(self.ship3_1)


        self.ship3_2 = Ship(102,32)
        self.ship3_2.rect.x = 391
        self.ship3_2.rect.y = 291
        self.ship_sprites.add(self.ship3_2)

        self.ship2_1 = Ship(67,32)
        self.ship2_1.rect.x = 391
        self.ship2_1.rect.y = 291
        self.ship_sprites.add(self.ship2_1)

        self.ship2_2 = Ship(67,32)
        self.ship2_2.rect.x = 391
        self.ship2_2.rect.y = 291
        self.ship_sprites.add(self.ship2_2)


        self.ship2_3 = Ship(67,32)
        self.ship2_3.rect.x = 391
        self.ship2_3.rect.y = 291
        self.ship_sprites.add(self.ship2_3)


        self.ship1_4 = Ship(32,32)
        self.ship1_4.rect.x = 391
        self.ship1_4.rect.y = 291
        self.ship_sprites.add(self.ship1_4)

        self.ship1_1 = Ship(32,32)
        self.ship1_1.rect.x = 391
        self.ship1_1.rect.y = 291
        self.ship_sprites.add(self.ship1_1)

        self.ship1_2 = Ship(32,32)
        self.ship1_2.rect.x = 391
        self.ship1_2.rect.y = 291
        self.ship_sprites.add(self.ship1_2)


        self.ship1_3 = Ship(32,32)
        self.ship1_3.rect.x = 391
        self.ship1_3.rect.y = 291
        self.ship_sprites.add(self.ship1_3)

        self.aim = Aim()
        self.aim.rect.x = 21
        self.aim.rect.y =21
        self.aim_group.add(self.aim)

        self.menu1 = MenuElement(' CONTINUE', 200, False)
        self.menu_group.add(self.menu1)
        
        self.menu2 = MenuElement(' SETTINGS', 260, False)
        self.menu_group.add(self.menu2)

        self.menu3 = MenuElement(' CONTROLS', 320, False)
        self.menu_group.add(self.menu3)

        self.menu4 = MenuElement('     QUIT', 380, False)
        self.menu_group.add(self.menu4)
        

        self.mmenu1 = MainMenuElement('NEW GAME', 200, True)
        self.main_menu_group.add(self.mmenu1)
        
        self.mmenu2 = MainMenuElement(' SETTINGS', 260, True)
        self.main_menu_group.add(self.mmenu2)

        self.mmenu3 = MainMenuElement('CONTROLS', 320, True)
        self.main_menu_group.add(self.mmenu3)

        self.mmenu4 = MainMenuElement('      QUIT', 380, True)
        self.main_menu_group.add(self.mmenu4)

        self.gameover_window = Gameover_window()
        self.gameover_group.add(self.gameover_window)



        self.cpu_board = []
        for i in range(10):
            self.cpu_board.append([])

        for m in self.cpu_board:
            for i in range(10):
                m.append('0')

        self.pla_board = []
        for i in range(10):
            self.pla_board.append([])

        for m in self.pla_board:
            for i in range(10):
                m.append('0')


        set_ships(self.cpu_board)
        put_boards(self.pla_board, self.cpu_board, self.descartes_p, self.descartes_cpu, self.p_cells, self.cpu_cells)


    def controller(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return True


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ys = -35

                    if self.pause or self.window == 'main':
                        self.menu_choice -= 1
                        if self.menu_choice < 0:
                            self.menu_choice = 0

                        
                elif event.key == pygame.K_LEFT:
                    self.xs = -35

                            
                elif event.key == pygame.K_RIGHT:
                    self.xs = 35

                            
                elif event.key == pygame.K_DOWN:
                    self.ys = 35
                    
                    if self.pause or self.window == 'main':
                        self.menu_choice += 1
                        if self.menu_choice > 3:
                            self.menu_choice = 3
                            
                        


                elif event.key == pygame.K_SPACE:
                    
                    self.set_ship -= 1
                    ship_coord_check(self.descartes_p, self.all_sprites,self. pla_board, self.set_ship)
                    
                elif event.key == pygame.K_RETURN:
                    if self.cpu_player > 0:
                        self.res_p = res_check(self.descartes_cpu, self.aim, self.cpu_board)
                        
                        hit_coord_check(self.descartes_cpu, self.aim, self.cpu_board)
                        self.cpu_player = (-1)*self.cpu_player

                    if self.pause or self.window == 'main':
                        self.menu_pick = True
                        if self.menu_choice == 3 and self.menu_pick:
                            return True
                        
                elif event.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
                    self.menu_choice = 0
                    


                

                elif event.key == pygame.K_w:
                    self.set_ship += 1
                

                elif event.key == pygame.K_TAB:
                    if self.set_ship == 10:
                        self.ship4.rotate()
                    if self.set_ship == 9:
                        self.ship3_1.rotate()
                    if self.set_ship == 8:
                        self.ship3_2.rotate()
                    if self.set_ship == 7:
                        self.ship2_1.rotate()
                    if self.set_ship == 6:
                        self.ship2_2.rotate()
                    if self.set_ship == 5:
                        self.ship2_3.rotate()




                        

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ys = 0
                if event.key == pygame.K_LEFT:
                    self.xs=0

                elif event.key == pygame.K_RIGHT:
                    self.xs = 0

                elif event.key == pygame.K_DOWN:
                    self.ys = 0
                    
                elif event.key == pygame.K_RETURN:
                    self.menu_pick = False


                        
                    
        return False

    
    def run_logic(self):
        if self.window == 'main':
            if self.menu_choice == 0:
                    (self.mmenu1.is_chosen, self.mmenu2.is_chosen,self.mmenu3.is_chosen, self.mmenu4.is_chosen) = (True, False, False, False)
                    if self.menu_pick:
                        self.window = 'game'
                    

            elif self.menu_choice == 1:
                (self.mmenu1.is_chosen, self.mmenu2.is_chosen,self.mmenu3.is_chosen, self.mmenu4.is_chosen) = (False,True, False, False)
                    
            elif self.menu_choice == 2:
                (self.mmenu1.is_chosen, self.mmenu2.is_chosen,self.mmenu3.is_chosen, self.mmenu4.is_chosen) = (False,False, True, False)

            elif self.menu_choice == 3:
                (self.mmenu1.is_chosen, self.mmenu2.is_chosen,self.mmenu3.is_chosen, self.mmenu4.is_chosen) = (False,False, False, True)

            self.mmenu1.update()
            self.mmenu2.update()
            self.mmenu3.update()
            self.mmenu4.update()
            
        elif self.window == 'game':
            if self.pause:
                if self.menu_choice == 0:
                    (self.menu1.is_chosen, self.menu2.is_chosen,self.menu3.is_chosen, self.menu4.is_chosen) = (True, False, False, False)
                    if self.menu_pick:
                        self.pause = False
                    

                elif self.menu_choice == 1:
                    (self.menu1.is_chosen, self.menu2.is_chosen,self.menu3.is_chosen, self.menu4.is_chosen) = (False,True, False, False)
                    
                elif self.menu_choice == 2:
                    (self.menu1.is_chosen, self.menu2.is_chosen,self.menu3.is_chosen, self.menu4.is_chosen) = (False,False, True, False)

                elif self.menu_choice == 3:
                    (self.menu1.is_chosen, self.menu2.is_chosen,self.menu3.is_chosen, self.menu4.is_chosen) = (False,False, False, True)

                self.menu1.update()
                self.menu2.update()
                self.menu3.update()
                self.menu4.update()
                
            if not self.pause:
                for ship in self.ship_sprites:
                    if ship.rect.x + ship.w > 710 and self.xs == 35:
                        ship.x_shift = 0
                        
                    elif ship.rect.x < 400 and self.xs == -35:
                        ship.x_shift = 0
                    else:
                        ship.x_shift = self.xs

                    if ship.rect.y + ship.h > 630 and self.ys == 35:
                        ship.y_shift = 0
                        
                    elif ship.rect.y < 300 and self.ys == -35:
                        ship.y_shift = 0
                    else:
                        ship.y_shift = self.ys
                        
                    
                        
                    

                if self.aim.rect.x > 301 and self.xs == 35:
                    self.aim.x_shift = 0

                elif self.aim.rect.x < 56 and self.xs == -35:
                    self.aim.x_shift = 0
                    
                else:
                    self.aim.x_shift = self.xs


                if self.aim.rect.y > 301 and self.ys == 35:
                    self.aim.y_shift = 0

                elif self.aim.rect.y < 56 and self.ys == -35:
                    self.aim.y_shift = 0
                    
                else:
                    self.aim.y_shift = self.ys




                if self.set_ship == 10:
                    self.ship4.update()

                elif self.set_ship == 9:
                    self.all_sprites.add(self.ship3_1)
                    self.ship3_1.update()
                    
                elif self.set_ship == 8:
                    self.all_sprites.add(self.ship3_2)
                    self.ship3_2.update()

                elif self.set_ship == 7:
                    self.all_sprites.add(self.ship2_1)
                    self.ship2_1.update()

                elif self.set_ship == 6:
                    self.all_sprites.add(self.ship2_2)
                    self.ship2_2.update()

                elif self.set_ship == 5:
                    self.all_sprites.add(self.ship2_3)
                    self.ship2_3.update()
                elif self.set_ship == 4:
                    self.all_sprites.add(self.ship1_1)
                    self.ship1_1.update()

                elif self.set_ship == 3:
                    self.all_sprites.add(self.ship1_2)
                    self.ship1_2.update()

                elif self.set_ship == 2:
                    self.all_sprites.add(self.ship1_3)
                    self.ship1_3.update()

                elif self.set_ship == 1:
                    self.all_sprites.add(self.ship1_4)
                    self.ship1_4.update()
                    
                elif self.set_ship == 0:
                    self.cpu_player = 1
                    self.set_ship -= 1




                if self.cpu_player > 0:
                    if self.res == 'hit':
                        self.cpu_player = -1

                    self.aim.update()
                    
                    


                elif self.cpu_player < 0:
                    if self.res_p == 'hit' or self.res_p == 'wrong':
                        
                        self.cpu_player = 1


                    elif self.res_p == 'miss':
                    

                        self.res = process_cpu_shot(self.pla_board)
                        self.cpu_player = (-1)*self.cpu_player

                if win_lose(self.pla_board, self.cpu_board) == 'cpu':
                    self.gameover = 'cpu'
                    
                elif win_lose(self.pla_board, self.cpu_board) == 'player':
                    self.gameover = 'player'




                
    def display_frame(self, screen):
        if self.window == 'main':
            screen.blit(menu_image, [0,0])
            self.main_menu_group.draw(screen)

##        elif self.window == 'gamover_cpu':
##            screen.fill((0,0,0))
##            f = pygame.font.Font(None, 40)
##
##            game_over = f.render("GAME OVER\n\n  CPU WINS!!!:  ",True,(227,14,53))
##            screen.blit(game_over, [200,200])
##
##        elif self.window == 'gamover_pla':
##            screen.fill((20,20,20))
##            f = pygame.font.Font(None, 40)
##
##            game_over = f.render("GAME OVER...  PLAYER WINS!!!:  ",True,(227,14,53))
##            screen.blit(game_over, [200,200])
            
            
            
            

            
        elif self.window == 'game':

            self.player_screen.fill((0,0,200))
            self.cpu_screen.fill(back_color)

            screen.blit(background_image, [0,0])          
            
            screen.blit(self.player_screen, (390, 290))
            screen.blit(self.cpu_screen, (20,20))

      
            self.cpu_cells.draw(screen)
            self.p_cells.draw(screen)
            self.all_sprites.draw(screen)
            self.dam_cells.draw(screen)

            
                
            if self.cpu_player > 0:
                self.aim_group.draw(screen)

            if self.pause == True:
                self.menu_group.draw(screen)

            if self.gameover == 'cpu':
                self.gameover_window.update('CPU WINS!!!  ')
                self.gameover_group.draw(screen)

            elif self.gameover == 'player':
                self.gameover_window.update("PLAYER WINS!!!  ")
                self.gameover_group.draw(screen)

            
            update_boards(screen, self.pla_board, self.cpu_board, self.descartes_p, self.descartes_cpu, self.p_cells, self.cpu_cells, self.dam_cells) 

        pygame.display.flip()




        





        
    
