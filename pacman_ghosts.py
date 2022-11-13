from copy import deepcopy
from math import sqrt
from random import choice

from pacman_entity import *

# dictionary with direction vectors (change in column, change in row)

OPPOSITE_DIRECTION = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}

BLUE_GHOST = []
for idx in range(1, 3):
    BLUE_GHOST.append(pygame.transform.scale(
        pygame.image.load(os.path.join('assets/ms_pacman', f'blue_ghost{idx}.png')), (E_SIZE, E_SIZE)))

EYES = pygame.transform.scale(pygame.image.load(os.path.join('assets/ms_pacman', 'eyes.png')), (E_SIZE, E_SIZE))


# Abstract class which is base for ghost
class Ghost(Entity, ABC):
    def __init__(self, x, y, image):
        self.target = (13 * TILE_SIZE, 12 * TILE_SIZE)
        self.next_tile = None
        self.in_box = True
        self.eaten = False
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/ms_pacman', f'{image}.png')), (E_SIZE, E_SIZE))

        super().__init__(x, y)

    # Draws ghost image based on his state
    def draw(self, win, frightened_flag, counter):
        if self.eaten:
            win.blit(EYES, (self.x, self.y))
        elif frightened_flag == 1:
            win.blit(BLUE_GHOST[0], (self.x, self.y))
        elif frightened_flag == 2:
            win.blit(BLUE_GHOST[counter], (self.x, self.y))
        else:
            win.blit(self.image, (self.x, self.y))

    # calculate which direction is closest to target
    def change_direction(self):
        distances = []

        for direction in self.tile.allowed_direction:
            if OPPOSITE_DIRECTION[direction] is not self.direction:
                distance = abs(sqrt((self.target[0] - (self.x + DIRECTIONS[direction][0] * TILE_SIZE)) ** 2 +
                                    (self.target[1] - (self.y + DIRECTIONS[direction][1] * TILE_SIZE)) ** 2))
                distances.append((direction, distance))

        if len(distances) != 0:
            direction_tuple = min(distances, key=lambda dis: dis[1])
            self.direction = direction_tuple[0]

    # Calculates next tile based on current tile and direction
    def get_next_tile(self, map_list):
        if valid_tile(self.tile.row + DIRECTIONS[self.direction][1], self.tile.column + DIRECTIONS[self.direction][0]):
            self.next_tile = map_list[self.tile.row + DIRECTIONS[self.direction][1]][
                self.tile.column + DIRECTIONS[self.direction][0]]
        else:
            self.tile = Tile(-1, self.tile.row, 0)
            self.next_tile = map_list[self.tile.row][0 if self.x >= 800 else 27]

    # Moves ghost in given direction
    def move(self, map_list, frightened):
        # up and down
        if DIRECTIONS[self.direction][0] == 0:
            if self.y + E_SIZE // 2 != self.next_tile.y + TILE_SIZE // 2:
                self.y += self.speed * DIRECTIONS[self.direction][1]
            else:
                self.tile = self.next_tile
                self.change_direction() if not frightened or self.eaten else self.frightened_mode_direction()
                self.get_next_tile(map_list)

        # left and right
        else:
            if self.x + E_SIZE // 2 != self.next_tile.x + TILE_SIZE // 2:
                self.x += self.speed * DIRECTIONS[self.direction][0]
            else:
                self.tile = self.next_tile
                self.change_direction() if not frightened or self.eaten else self.frightened_mode_direction()
                self.get_next_tile(map_list)

    # Changes direction to opposite one
    def turn_around(self, map_list):
        if OPPOSITE_DIRECTION[self.direction] in self.tile.allowed_direction:
            self.direction = OPPOSITE_DIRECTION[self.direction]
            self.get_next_tile(map_list)

    # Chooses random direction from directions where ghost can go
    def frightened_mode_direction(self):
        if OPPOSITE_DIRECTION[self.direction] in self.tile.allowed_direction:
            direction_choice = deepcopy(self.tile.allowed_direction)
            direction_choice.remove(OPPOSITE_DIRECTION[self.direction])
            if len(direction_choice) != 0:
                self.direction = choice(direction_choice)
        else:
            if len(self.tile.allowed_direction) != 0:
                self.direction = choice(self.tile.allowed_direction)

    # Makes ghost go in start box
    def get_in_box(self, map_list):
        self.target = (13 * TILE_SIZE, 13 * TILE_SIZE)
        if self.tile == map_list[10][13]:
            self.direction = DOWN
            self.get_next_tile(map_list)
        elif self.tile == map_list[12][13]:
            self.eaten = False
            self.in_box = True


class Blinky(Ghost):
    # Blinky target when ghost are scattering
    def scatter(self):
        self.target = (PACMAN_WIN_WIDTH - 50, 0)

    # Blinky's target is Ms.Pac-Man
    def chase(self, player_x, player_y, player_direction):
        self.target = (player_x, player_y)


class Pinky(Ghost):
    def scatter(self):
        self.target = (50, 0)

    # Pinky's target is 4 tiles in front of Ms.Pac-Man
    def chase(self, player_x, player_y, player_direction):
        self.target = (player_x + DIRECTIONS[player_direction][0] * 4 * TILE_SIZE,
                       player_y + DIRECTIONS[player_direction][1] * 4 * TILE_SIZE)


class Inky(Ghost):
    def scatter(self):
        self.target = (PACMAN_WIN_WIDTH - 50, HEIGHT)

    # Inky's target is kind of difficult to calculate. Start point is two tiles in front of Ms.Pac-Man,
    # then we make line between start point and Blinky.
    # If we invert this line to opposite direction we get Inky's target.
    def chase(self, player_x, player_y, player_direction, blinky_x, blinky_y):
        start_point = (player_x + DIRECTIONS[player_direction][0] * 2 * TILE_SIZE,
                       player_y + DIRECTIONS[player_direction][1] * 2 * TILE_SIZE)
        start_to_blinky = (blinky_x - start_point[0], blinky_y - start_point[1])
        self.target = (start_point[0] + start_to_blinky[0] * -1, start_point[1] + start_to_blinky[1] * -1)


class Sue(Ghost):
    def scatter(self):
        self.target = (50, HEIGHT)

    # Sue's target is Ms.Pac-man if Sue is more than 8 tiles away. If Sue is closer her target is the same as when
    # ghosts scatter.
    def chase(self, player_x, player_y, player_direction):
        Sue_Pacman_distance = abs(sqrt((player_x - self.x) ** 2 + (player_y - self.y) ** 2))
        if Sue_Pacman_distance > TILE_SIZE * 8:
            self.target = (player_x, player_y)
        else:
            self.scatter()
