import pygame
from .Game import Game
from .PyPlayer import PyPlayer
from .ui.aim import Aim
from .ui.gameover import GameOver


class PyPlay(Game):

    ship_setup = False

    def __init__(self):
        self.aim = Aim()
        self.aim_group = pygame.sprite.Group()
        self.aim_group.add(self.aim)
        self.gameover = pygame.sprite.Group()

    def start(self):
        Game.start(self, 10, 1)

    def initialize(self):
        pygame.key.set_repeat(500, 30)

    def place_ship(self):
        if not self.curr_player.board.managed_ship:
            return

        board = self.curr_player.board
        ship = board.managed_ship
        success = board.place_ship(ship)

        if not self.curr_player.setup_next_ship(success):
            board.managed_ship = None
            self.curr_player.stage = "scanning"

    def rotate_ship(self):
        if not self.curr_player.board.managed_ship:
            return

        board = self.curr_player.board
        ship = board.managed_ship
        board.managed_ship = board.rotate_ship(ship)

    def move_ship(self, course):
        if not self.curr_player.board.managed_ship:
            return

        board = self.curr_player.board
        ship = board.managed_ship
        board.move_ship(ship, course)

    def move_aim(self, course):
        if course == 'up':
            self.aim.dy -= 1
        elif course == 'down':
            self.aim.dy += 1
        elif course == 'left':
            self.aim.dx -= 1
        elif course == 'right':
            self.aim.dx += 1

    def hit(self):
        if self.curr_player.board.managed_ship:
            return

        # player
        h = self.curr_opponent.on_fire(self.aim.x, self.aim.y)
        self.game_over = (len(self.curr_opponent.board.ships) == 0)

        if self.game_over:
            self.finish_round("You win")
            return

        # bot
        if not h:
            self.curr_player.stage = "waiting"
            self.swap_players()
            while not self.game_over and self.turn():
                pass
            if self.game_over:
                self.finish_round("You lose")
                return

        self.curr_player.stage = "scanning"

    def finish_round(self, text):
        self.gameover.empty()
        self.gameover.add(GameOver(text))

    def composite(self):
        player_id = len(self.players)
        return PyPlayer(player_id)

    def get_sprites(self):
        sprites = []
        for p in self.players:
            sprites = sprites + p.board.draw_list
        if self.curr_player.human and not self.curr_player.board.managed_ship:
            sprites.append(self.aim_group)
        if self.game_over and len(self.gameover.sprites()) > 0:
            sprites.append(self.gameover)

        return sprites
