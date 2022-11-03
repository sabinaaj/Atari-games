import pygame
import os
from constants import *

MAP = [
    [12,6,6,6,6,6,6,13,12,6,6,6,6,6,6,6,6,6,6,13,12,6,6,6,6,6,6,13],
    [5,0,0,0,0,0,0,3,5,0,0,0,0,0,0,0,0,0,0,3,5,0,0,0,0,0,0,3],
    [5,0,8,4,4,9,0,3,5,0,8,4,4,4,4,4,4,9,0,3,5,0,8,4,4,9,0,3],
    [5,2,7,6,6,10,0,7,10,0,7,6,6,6,6,6,6,10,0,7,10,0,7,6,6,10,2,3],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [15,4,9,0,8,9,0,8,4,4,4,9,0,8,9,0,8,4,4,4,9,0,8,9,0,8,4,14],
    [6,6,10,0,3,5,0,7,6,6,6,10,0,3,5,0,7,6,6,6,10,0,3,5,0,7,6,6],
    [1,1,1,0,3,5,0,0,0,0,0,0,0,3,5,0,0,0,0,0,0,0,3,5,0,1,1,1],
    [4,4,9,0,3,15,4,4,9,1,8,4,4,14,15,4,4,9,1,8,4,4,14,5,0,8,4,4],
    [1,1,5,0,7,6,6,6,10,1,7,6,6,6,6,6,6,10,1,7,6,6,6,10,0,3,1,1],
    [1,1,5,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,3,1,1],
    [1,1,5,0,8,4,4,4,9,1,8,4,4,11,11,4,4,9,1,8,4,4,4,9,0,3,1,1],
    [1,1,5,0,3,12,6,6,10,1,3,1,1,1,1,1,1,5,1,7,6,6,13,5,0,3,1,1],
    [1,1,5,0,3,5,1,1,1,1,3,1,1,1,1,1,1,5,1,1,1,1,3,5,0,3,1,1],
    [1,1,5,0,3,5,1,8,9,1,3,1,1,1,1,1,1,5,1,8,9,1,3,5,0,3,1,1],
    [6,6,10,0,7,10,1,3,5,1,7,6,6,6,6,6,6,10,1,3,5,1,7,10,0,7,6,6],
    [1,1,1,0,1,1,1,3,5,1,1,1,1,1,1,1,1,1,1,3,5,1,1,1,0,1,1,1],
    [4,4,9,0,8,4,4,14,15,4,4,9,1,8,9,1,8,4,4,14,15,4,4,9,0,8,4,4],
    [1,1,5,0,7,6,6,6,6,6,6,10,1,3,5,1,7,6,6,6,6,6,6,10,0,3,1,1],
    [1,1,5,0,0,0,0,0,0,0,1,1,1,3,5,1,1,1,0,0,0,0,0,0,0,3,1,1],
    [1,1,5,0,8,4,4,4,9,0,8,4,4,14,15,4,4,9,0,8,4,4,4,9,0,3,1,1],
    [12,6,10,0,7,6,6,6,10,0,7,6,6,6,6,6,6,10,0,7,6,6,6,10,0,7,6,13],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [5,0,8,4,4,9,0,8,4,4,4,9,0,8,9,0,8,4,4,4,9,0,8,4,4,9,0,3],
    [5,0,3,16,16,5,0,3,12,6,6,10,0,3,5,0,7,6,6,13,5,0,3,16,16,5,0,3],
    [5,0,3,16,16,5,0,3,5,0,0,0,0,3,5,0,0,0,0,3,5,0,3,16,16,5,0,3],
    [5,2,3,16,16,5,0,3,5,0,8,4,4,14,15,4,4,9,0,3,5,0,3,16,16,5,2,3],
    [5,0,7,6,6,10,0,7,10,0,7,6,6,6,6,6,6,10,0,7,10,0,7,6,6,10,0,3],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
    [15,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,14]
]

TILE_SIZE = 30
DOT_RADIUS = 5
BLUE = (0,181,226)

WALL1 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/ms_pacman', 'wall1.png')), (TILE_SIZE, TILE_SIZE))
WALL2 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/ms_pacman', 'wall2.png')), (TILE_SIZE, TILE_SIZE))
WALL3 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/ms_pacman', 'wall3.png')), (TILE_SIZE, TILE_SIZE))
WALL4 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/ms_pacman', 'wall4.png')), (TILE_SIZE, TILE_SIZE))
WALL5 = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/ms_pacman', 'wall5.png')), (TILE_SIZE, TILE_SIZE))

class Map:
    def __init__(self):
        self.rows = 30
        self.columns = 28

    def draw(self, win):
        for row_idx in range(self.rows):
            for col_idx in range(self.columns):
                x = col_idx * TILE_SIZE
                y = 50 +  row_idx * TILE_SIZE
                self.draw_tile(win, x, y, MAP[row_idx][col_idx])
        pygame.display.update()

    def draw_tile(self, win, x, y, tile_type):
        if tile_type == 0:
            pygame.draw.circle(win, BLUE,(x + TILE_SIZE // 2, y + TILE_SIZE // 2), 5)
        elif tile_type == 2:
            pygame.draw.circle(win, BLUE, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), 10)
        elif tile_type == 3:
            win.blit(WALL1, (x, y))
        elif tile_type == 4:
            win.blit(pygame.transform.rotate(WALL1, 270), (x, y))
        elif tile_type == 5:
            win.blit(pygame.transform.rotate(WALL1, 180), (x, y))
        elif tile_type == 6:
            win.blit(pygame.transform.rotate(WALL1, 90), (x, y))
        elif tile_type == 7:
            win.blit(WALL2, (x, y))
        elif tile_type == 8:
            win.blit(pygame.transform.rotate(WALL2, 270), (x, y))
        elif tile_type == 9:
            win.blit(pygame.transform.rotate(WALL2, 180), (x, y))
        elif tile_type == 10:
            win.blit(pygame.transform.rotate(WALL2, 90), (x, y))
        elif tile_type == 11:
            win.blit(pygame.transform.rotate(WALL3, 270), (x, y))
        elif tile_type == 12:
            win.blit(WALL4, (x, y))
        elif tile_type == 13:
            win.blit(pygame.transform.rotate(WALL4, 270), (x, y))
        elif tile_type == 14:
            win.blit(pygame.transform.rotate(WALL4, 180), (x, y))
        elif tile_type == 15:
            win.blit(pygame.transform.rotate(WALL4, 90), (x, y))
        elif tile_type == 16:
            win.blit(WALL5, (x, y))


