from pacman_entity import *


class Player(Entity):
    def __init__(self, x, y):
        self.images = []
        for image in range(1, 5):
            self.images.append(pygame.transform.scale(
                pygame.image.load(os.path.join('assets/ms_pacman', f'Ms.pac-man{image}.png')), (E_SIZE, E_SIZE)))

        super().__init__(x, y)

    def draw(self, win, counter):
        if self.direction == LEFT or self.direction is None:
            win.blit(self.images[counter], (self.x, self.y))
        elif self.direction == DOWN:
            win.blit(pygame.transform.rotate(self.images[counter], 90), (self.x, self.y))
        elif self.direction == RIGHT:
            win.blit(pygame.transform.flip(self.images[counter], True, False), (self.x, self.y))
        elif self.direction == UP:
            win.blit(pygame.transform.rotate(self.images[counter], 270), (self.x, self.y))

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

    def change_direction(self, direction):
        if direction in self.tile.allowed_direction:
            if (direction == RIGHT or direction == LEFT) and self.x <= self.tile.x + TILE_SIZE // 2 <= self.x + E_SIZE:
                self.direction = direction
            elif (direction == DOWN or direction == UP) and self.y <= self.tile.y + TILE_SIZE // 2 <= self.y + E_SIZE:
                self.direction = direction

    def eat_pellet(self):
        if self.tile.tile_type == 1:
            if self.x <= self.tile.x + TILE_SIZE // 2 <= self.x + E_SIZE:
                self.tile.tile_type = 0

    def eat_power_pellet(self):
        if self.tile.tile_type == 2:
            if self.x <= self.tile.x + TILE_SIZE // 2 <= self.x + E_SIZE:
                self.tile.tile_type = 0
                return True
            else:
                return False
