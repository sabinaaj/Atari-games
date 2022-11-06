from pacman_map import *

E_SPEED = 5
E_SIZE = 40


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile = None
        self.direction = None

    def change_direction(self, direction):
        if direction in self.tile.allowed_direction:
            self.direction = direction

    def move(self):
        if self.direction == LEFT:
            if LEFT in self.tile.allowed_direction:
                self.x -= E_SPEED
            else:
                if self.x > self.tile.x:
                    self.x -= E_SPEED

        elif self.direction == RIGHT:
            if RIGHT in self.tile.allowed_direction:
                self.x += E_SPEED
            else:
                if self.x + E_SIZE < self.tile.x + TILE_SIZE:
                    self.x += E_SPEED

        elif self.direction == DOWN:
            if DOWN in self.tile.allowed_direction:
                self.y += E_SPEED
            else:
                if self.y + E_SIZE < self.tile.y + TILE_SIZE:
                    self.y += E_SPEED

        elif self.direction == UP:
            if UP in self.tile.allowed_direction:
                self.y -= E_SPEED
            else:
                if self.y > self.tile.y:
                    self.y -= E_SPEED

    def check_position(self, map_list):
        row = ((self.y + E_SIZE // 2) - 50) // TILE_SIZE
        column = (self.x + E_SIZE // 2) // TILE_SIZE
        self.tile = map_list[row][column]
        #print(f'{self.y + E_SIZE // 2} row: {row}, col:{column}, type: {self.tile.tile_type}, {self.tile.allowed_direction}')
