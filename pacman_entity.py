from pacman_map import *
from abc import ABC

E_SPEED = 5
E_SIZE = 40


class Entity(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile = None
        self.next_tile = None
        self.direction = None


    def check_position(self, map_list):
        row = ((self.y + E_SIZE // 2) - 50) // TILE_SIZE
        column = (self.x + E_SIZE // 2) // TILE_SIZE
        if valid_tile(row, column):
            self.tile = map_list[row][column]
        #print(f'{self.y + E_SIZE // 2} row: {row}, col:{column}, type: {self.tile.tile_type}, {self.tile.allowed_direction}')

    def go_through_tunnel(self):
        if self.x + E_SIZE <= 0:
            self.x = PACMAN_WIN_WIDTH
        elif self.x >= PACMAN_WIN_WIDTH:
            self.x = 0 - E_SIZE

