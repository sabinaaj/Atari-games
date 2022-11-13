from abc import ABC

from pacman_map import *

E_SIZE = 40

DIRECTIONS = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0),
    None: (0, 0),
}


# Abstract class which is base for players and ghosts
class Entity(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.tile = None
        self.direction = None

    # Checks on which tile is entity is standing
    def check_position(self, map_list):
        row = ((self.y + E_SIZE // 2) - 50) // TILE_SIZE
        column = (self.x + E_SIZE // 2) // TILE_SIZE
        if valid_tile(row, column):
            self.tile = map_list[row][column]

    # Teleports entity at other end of the screen
    def go_through_tunnel(self):
        if self.x + E_SIZE <= 0:
            self.x = PACMAN_WIN_WIDTH
        elif self.x >= PACMAN_WIN_WIDTH:
            self.x = 0 - E_SIZE
