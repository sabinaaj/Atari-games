from pacman_entity import *


class Player(Entity):
    def __init__(self, x, y):
        self.images = []
        for image in range(1,5):
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

    def eat_circle(self):
        if self.tile.tile_type == 1:
            if self.x <= self.tile.x + TILE_SIZE // 2 <= self.x + E_SIZE:
                self.tile.tile_type = 0
