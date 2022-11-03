import pygame

from pacman_map import *
from pacman_player import *
from constants import *


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player(14 * TILE_SIZE - P_SIZE // 2, 22 * TILE_SIZE + 45)

    def draw(self, win):
        win.fill(DARK_GRAY)
        self.player.draw(win)

        self.map.draw(win)

        pygame.display.update()

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(LEFT)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(RIGHT)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.move(UP)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.move(DOWN)


def gameloop(win):
    run = True
    game = Game()
    win = pygame.display.set_mode((game.map.columns * TILE_SIZE, HEIGHT), pygame.RESIZABLE)

    while run:
        pygame.time.Clock().tick(FPS)

        keys = pygame.key.get_pressed()
        game.player_movement(keys)

        game.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


