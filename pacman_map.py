from constants import *

# 2D list of map tiles types
MAP = [
    [12, 6, 6, 6, 6, 6, 6, 13, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 13, 12, 6, 6, 6, 6, 6, 6, 13],
    [5, 1, 1, 1, 1, 1, 1, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 1, 1, 1, 1, 1, 1, 3],
    [5, 1, 8, 4, 4, 9, 1, 3, 5, 1, 8, 4, 4, 4, 4, 4, 4, 9, 1, 3, 5, 1, 8, 4, 4, 9, 1, 3],
    [5, 2, 7, 6, 6, 10, 1, 7, 10, 1, 7, 6, 6, 6, 6, 6, 6, 10, 1, 7, 10, 1, 7, 6, 6, 10, 2, 3],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [15, 4, 9, 1, 8, 9, 1, 8, 4, 4, 4, 9, 1, 8, 9, 1, 8, 4, 4, 4, 9, 1, 8, 9, 1, 8, 4, 14],
    [6, 6, 10, 1, 3, 5, 1, 7, 6, 6, 6, 10, 1, 3, 5, 1, 7, 6, 6, 6, 10, 1, 3, 5, 1, 7, 6, 6],
    [0, 0, 0, 1, 3, 5, 1, 1, 1, 1, 1, 1, 1, 3, 5, 1, 1, 1, 1, 1, 1, 1, 3, 5, 1, 0, 0, 0],
    [4, 4, 9, 1, 3, 15, 4, 4, 9, 0, 8, 4, 4, 14, 15, 4, 4, 9, 0, 8, 4, 4, 14, 5, 1, 8, 4, 4],
    [0, 0, 5, 1, 7, 6, 6, 6, 10, 0, 7, 6, 6, 6, 6, 6, 6, 10, 0, 7, 6, 6, 6, 10, 1, 3, 0, 0],
    [0, 0, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0],
    [0, 0, 5, 1, 8, 4, 4, 4, 9, 0, 8, 4, 4, 11, 11, 4, 4, 9, 0, 8, 4, 4, 4, 9, 1, 3, 0, 0],
    [0, 0, 5, 1, 3, 12, 6, 6, 10, 0, 3, 0, 0, 0, 0, 0, 0, 5, 0, 7, 6, 6, 13, 5, 1, 3, 0, 0],
    [0, 0, 5, 1, 3, 5, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 3, 5, 1, 3, 0, 0],
    [0, 0, 5, 1, 3, 5, 0, 8, 9, 0, 3, 0, 0, 0, 0, 0, 0, 5, 0, 8, 9, 0, 3, 5, 1, 3, 0, 0],
    [6, 6, 10, 1, 7, 10, 0, 3, 5, 0, 7, 6, 6, 6, 6, 6, 6, 10, 0, 3, 5, 0, 7, 10, 1, 7, 6, 6],
    [0, 0, 0, 1, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 0, 0, 0, 1, 0, 0, 0],
    [4, 4, 9, 1, 8, 4, 4, 14, 15, 4, 4, 9, 0, 8, 9, 0, 8, 4, 4, 14, 15, 4, 4, 9, 1, 8, 4, 4],
    [0, 0, 5, 1, 7, 6, 6, 6, 6, 6, 6, 10, 0, 3, 5, 0, 7, 6, 6, 6, 6, 6, 6, 10, 1, 3, 0, 0],
    [0, 0, 5, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 3, 5, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0],
    [0, 0, 5, 1, 8, 4, 4, 4, 9, 1, 8, 4, 4, 14, 15, 4, 4, 9, 1, 8, 4, 4, 4, 9, 1, 3, 0, 0],
    [12, 6, 10, 1, 7, 6, 6, 6, 10, 1, 7, 6, 6, 6, 6, 6, 6, 10, 1, 7, 6, 6, 6, 10, 1, 7, 6, 13],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [5, 1, 8, 4, 4, 9, 1, 8, 4, 4, 4, 9, 1, 8, 9, 1, 8, 4, 4, 4, 9, 1, 8, 4, 4, 9, 1, 3],
    [5, 1, 3, 16, 16, 5, 1, 3, 12, 6, 6, 10, 1, 3, 5, 1, 7, 6, 6, 13, 5, 1, 3, 16, 16, 5, 1, 3],
    [5, 1, 3, 16, 16, 5, 1, 3, 5, 1, 1, 1, 1, 3, 5, 1, 1, 1, 1, 3, 5, 1, 3, 16, 16, 5, 1, 3],
    [5, 2, 3, 16, 16, 5, 1, 3, 5, 1, 8, 4, 4, 14, 15, 4, 4, 9, 1, 3, 5, 1, 3, 16, 16, 5, 2, 3],
    [5, 1, 7, 6, 6, 10, 1, 7, 10, 1, 7, 6, 6, 6, 6, 6, 6, 10, 1, 7, 10, 1, 7, 6, 6, 10, 1, 3],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [15, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 14]
]

ROWS, COLS = 30, 28
TILE_SIZE = 30
DOT_RADIUS = 5
BLUE = (0, 181, 226)

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
        self.map_list = []
        self.pellets = 0

    # Makes list of all tiles in map
    def get_map(self):
        self.map_list = [[Tile(col_idx, row_idx, MAP[row_idx][col_idx])
                          for col_idx in range(COLS)] for row_idx in range(ROWS)]

        for row_idx in range(ROWS):
            for col_idx in range(COLS):
                self.map_list[row_idx][col_idx].allowed_direction = self.check_allowed_directions(row_idx, col_idx)

    # Draws all tiles of the map
    def draw(self, win):
        for row_idx in range(ROWS):
            for col_idx in range(COLS):
                self.map_list[row_idx][col_idx].draw(win)

    # Makes list of directions where entity can go from that tile
    def check_allowed_directions(self, row_idx, col_idx):
        allowed_direction = []

        # ghost can go out of their box
        if (row_idx == 11 or row_idx == 12) and (col_idx == 13 or col_idx == 14):
            allowed_direction.append(UP)

        if self.map_list[row_idx][col_idx].tile_type >= 3:
            return allowed_direction

        # counts pellets in map
        if 1 <= self.map_list[row_idx][col_idx].tile_type <= 2:
            self.pellets += 1

        if valid_tile(row_idx, col_idx - 1):
            if self.map_list[row_idx][col_idx - 1].can_go:
                allowed_direction.append(LEFT)
        else:
            allowed_direction.append(LEFT)  # entity can go through tunnel

        if valid_tile(row_idx, col_idx + 1):
            if self.map_list[row_idx][col_idx + 1].can_go:
                allowed_direction.append(RIGHT)
        else:
            allowed_direction.append(RIGHT)

        if valid_tile(row_idx + 1, col_idx):
            if self.map_list[row_idx + 1][col_idx].can_go:
                allowed_direction.append(DOWN)

        if valid_tile(row_idx - 1, col_idx):
            if self.map_list[row_idx - 1][col_idx].can_go:
                allowed_direction.append(UP)

        return allowed_direction


# Checks if tile is in map
def valid_tile(row, col):
    if 0 <= col <= 27 and 0 <= row <= 29:
        return True
    else:
        return False


class Tile:
    # (if entity can step on, tile image, rotation of tile image)
    TILE_TYPES = [
        (True, None, 0),
        (True, None, 0),
        (True, None, 0),
        (False, WALL1, 0),
        (False, WALL1, 270),
        (False, WALL1, 180),
        (False, WALL1, 90),
        (False, WALL2, 0),
        (False, WALL2, 270),
        (False, WALL2, 180),
        (False, WALL2, 90),
        (False, WALL3, 270),
        (False, WALL4, 0),
        (False, WALL4, 270),
        (False, WALL4, 180),
        (False, WALL4, 90),
        (False, WALL5, 0),
    ]

    def __init__(self, column, row, tile_type):
        self.column = column
        self.row = row
        self.x = column * TILE_SIZE
        self.y = row * TILE_SIZE + 50
        self.tile_type = tile_type
        self.allowed_direction = []
        self.can_go, self.image, self.rotation = self.TILE_TYPES[tile_type]

    # Draws tile image or makes circle for pellets
    def draw(self, win):
        if self.tile_type == 1 or self.tile_type == 2:
            pygame.draw.circle(win, BLUE, (self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2), 5 * self.tile_type)
        elif self.tile_type in range(3, 17):
            win.blit(pygame.transform.rotate(self.image, self.rotation), (self.x, self.y))
