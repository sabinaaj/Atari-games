from pacman_entity import *


class Player(Entity):
    def __init__(self, x, y):
        self.lives = 3
        self.score = 0
        self.images = []
        for image in range(1, 5):
            self.images.append(pygame.transform.scale(
                pygame.image.load(os.path.join('assets/ms_pacman', f'Ms.pac-man{image}.png')), (E_SIZE, E_SIZE)))

        super().__init__(x, y)

    # Draws pacman image based on direction and animation counter
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
        # up and down
        if DIRECTIONS[self.direction][0] == 0:
            if self.direction in self.tile.allowed_direction:
                self.y += self.speed * DIRECTIONS[self.direction][1]
            else:
                if self.direction == DOWN:
                    if self.y + E_SIZE < self.tile.y + TILE_SIZE:
                        self.y += self.speed
                else:
                    if self.y > self.tile.y:
                        self.y -= self.speed

        # left and right
        else:
            if self.direction in self.tile.allowed_direction:
                self.x += self.speed * DIRECTIONS[self.direction][0]
            else:
                if self.direction == LEFT:
                    if self.x > self.tile.x:
                        self.x -= self.speed
                else:
                    if self.x + E_SIZE < self.tile.x + TILE_SIZE:
                        self.x += self.speed

    # Changes player direction
    def change_direction(self, direction):
        if direction in self.tile.allowed_direction:
            self.direction = direction

    # Checks if player can eat given type of pellet
    def eat(self, tile_type, score):
        if self.tile.tile_type == tile_type:
            if self.x <= self.tile.x + TILE_SIZE // 2 <= self.x + E_SIZE:
                self.score += score
                self.tile.tile_type = 0
                return True
            else:
                return False

    def eat_pellet(self):
        return self.eat(1, 10)

    def eat_power_pellet(self):
        return self.eat(2, 50)
