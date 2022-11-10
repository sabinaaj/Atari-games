from math import sqrt
from random import choice
from pacman_entity import *

DIRECTIONS = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}

BLUE_GHOST = pygame.transform.scale(pygame.image.load(os.path.join('assets/ms_pacman', 'blue_ghost.png')), (E_SIZE, E_SIZE))
EYES = pygame.transform.scale(pygame.image.load(os.path.join('assets/ms_pacman', 'eyes.png')), (E_SIZE, E_SIZE))

class Ghost(Entity):
    def __init__(self, x, y, image):
        self.target = (13 * TILE_SIZE, 12 * TILE_SIZE)
        self.in_box = True
        self.eaten = False
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/ms_pacman', f'{image}.png')), (E_SIZE, E_SIZE))

        super().__init__(x, y)

    def draw(self, win, frightenedFlag):
        if frightenedFlag:
            win.blit(BLUE_GHOST, (self.x, self.y))
        elif self.eaten:
            win.blit(EYES, (self.x, self.y))
        else:
            win.blit(self.image, (self.x, self.y))

    def change_direction(self):
        distances = []
        # left
        if RIGHT is not self.direction and LEFT in self.tile.allowed_direction:
            distance = abs(sqrt((self.target[0] - (self.x - TILE_SIZE)) ** 2 + (self.target[1] - self.y) ** 2))
            distances.append((LEFT, distance))
        # right
        if LEFT is not self.direction and RIGHT in self.tile.allowed_direction:
            distance = abs(sqrt((self.target[0] - (self.x + TILE_SIZE)) ** 2 + (self.target[1] - self.y) ** 2))
            distances.append((RIGHT, distance))
        # down
        if UP is not self.direction and DOWN in self.tile.allowed_direction:
            distance = abs(sqrt((self.target[0] - self.x) ** 2 + (self.target[1] - (self.y + TILE_SIZE)) ** 2))
            distances.append((DOWN, distance))
        # up
        if DOWN is not self.direction and UP in self.tile.allowed_direction:
            distance = abs(sqrt((self.target[0] - self.x) ** 2 + (self.target[1] - (self.y - TILE_SIZE)) ** 2))
            distances.append((UP, distance))

        if len(distances) != 0:
            direction_tuple = min(distances, key=lambda dis: dis[1])
            self.direction = direction_tuple[0]

    def get_next_tile(self, map_list):
        if valid_tile(self.tile.row + DIRECTIONS[self.direction][1], self.tile.column + DIRECTIONS[self.direction][0]):
            self.next_tile = map_list[self.tile.row + DIRECTIONS[self.direction][1]][
                self.tile.column + DIRECTIONS[self.direction][0]]
        else:
            self.tile = Tile(-1, self.tile.row, 0)
            self.next_tile = map_list[self.tile.row][0 if self.x >= 800 else 27]

    def move(self, map_list, frightened):
        # up and down
        if DIRECTIONS[self.direction][0] == 0:
            if self.y + E_SIZE // 2 != self.next_tile.y + TILE_SIZE // 2:
                self.y += E_SPEED * DIRECTIONS[self.direction][1]
            else:
                self.tile = self.next_tile
                self.change_direction() if not frightened else self.frightened_mode_direction()
                self.get_next_tile(map_list)

        # left and right
        else:
            if self.x + E_SIZE // 2 != self.next_tile.x + TILE_SIZE // 2:
                self.x += E_SPEED * DIRECTIONS[self.direction][0]
            else:
                self.tile = self.next_tile
                self.change_direction() if not frightened else self.frightened_mode_direction()
                self.get_next_tile(map_list)
        # print(
        #     f'row: {self.tile.row}, col:{self.tile.column}, type: {self.tile.tile_type}, ')

    def turn_around(self, map_list):
        if self.direction == LEFT:
            self.direction = RIGHT
            self.get_next_tile(map_list)
        if self.direction == RIGHT:
            self.direction = LEFT
            self.get_next_tile(map_list)
        if self.direction == DOWN:
            self.direction = UP
            self.get_next_tile(map_list)
        if self.direction == UP:
            self.direction = DOWN
            self.get_next_tile(map_list)

    def frightened_mode_direction(self):
        self.direction = choice(self.tile.allowed_direction)



class Blinky(Ghost):
    def scatter(self):
        self.target = (PACMAN_WIN_WIDTH - 50, 0)

    def chase(self, player_x, player_y):
        self.target = (player_x, player_y)


class Pinky(Ghost):
    def scatter(self):
        self.target = (50, 0)

    def chase(self, player_x, player_y):
        self.target = (player_x, player_y)


class Inky(Ghost):
    def scatter(self):
        self.target = (PACMAN_WIN_WIDTH - 50, HEIGHT)

    def chase(self, player_x, player_y):
        self.target = (player_x, player_y)


class Sue(Ghost):
    def scatter(self):
        self.target = (50, HEIGHT)

    def chase(self, player_x, player_y):
        self.target = (player_x, player_y)
