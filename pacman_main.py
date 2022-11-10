from time import *

import pygame

from pacman_player import *
from pacman_ghosts import *


class Game:
    def __init__(self):
        self.map = Map()
        self.map.get_map()

        self.player = Player(13 * TILE_SIZE + E_SIZE // 2, 22 * TILE_SIZE + 45)
        self.counter = 0

        self.blinky = Blinky(11 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Blinky')
        self.pinky = Pinky(12 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Pinky')
        self.inky = Inky(14 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Inky')
        self.sue = Sue(15 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Sue')
        self.ghosts = [self.blinky, self.pinky, self.inky, self.sue]
        for ghost in self.ghosts:
            ghost.check_position(self.map.map_list)
            ghost.change_direction()
            ghost.get_next_tile(self.map.map_list)

        self.player.check_position(self.map.map_list)

        self.frightened = False
        self.chase = False


    def draw(self, win):
        win.fill(DARK_GRAY)

        self.map.draw(win)
        self.player.draw(win, self.counter // 5)

        for ghost in self.ghosts:
            ghost.draw(win, self.frightened)

        if self.counter >= 19:
            self.counter = 0
        else:
            self.counter += 1

        pygame.display.update()

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.change_direction(LEFT)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.change_direction(RIGHT)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.change_direction(UP)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.change_direction(DOWN)

    def player_handler(self, frightened_mode):
        self.player.check_position(self.map.map_list)
        self.player.eat_pellet()
        if self.player.eat_power_pellet():
            self.frightened = True
            pygame.time.set_timer(frightened_mode, 5000)
            for ghost in self.ghosts:
                ghost.turn_around(self.map.map_list)
        self.player.go_through_tunnel()
        self.player.move()

    def ghost_handler(self):
        for ghost in self.ghosts:

            if ghost.in_box:
                if ghost.tile == self.map.map_list[10][13]:
                    ghost.in_box = False
            else:
                if self.chase:
                    ghost.chase(self.player.x, self.player.y)
                else:
                    ghost.scatter()

            ghost.go_through_tunnel()
            ghost.move(self.map.map_list, self.frightened)



def gameloop():
    run = True
    win = pygame.display.set_mode((PACMAN_WIN_WIDTH, HEIGHT), pygame.RESIZABLE)

    game = Game()

    change_chase = pygame.USEREVENT
    pygame.time.set_timer(change_chase, 20000 if game.chase else 7000)

    frightened_mode = pygame.USEREVENT + 1

    while run:
        pygame.time.Clock().tick(FPS)

        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.player_handler(frightened_mode)

        game.ghost_handler()

        game.draw(win)

        for event in pygame.event.get():
            if event.type == change_chase:
                game.chase = not game.chase
                pygame.time.set_timer(change_chase, 20000 if game.chase else 5000)
            if event.type == frightened_mode:
                game.frightened = False
            if event.type == pygame.QUIT:
                run = False
