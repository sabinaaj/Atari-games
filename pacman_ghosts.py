from pacman_entity import *


class Blinky(Entity):
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
                pygame.image.load(os.path.join('assets/ms_pacman', 'Blinky.png')), (E_SIZE, E_SIZE))
        super().__init__(x, y)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

class Pinky(Entity):
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
                pygame.image.load(os.path.join('assets/ms_pacman', 'Pinky.png')), (E_SIZE, E_SIZE))
        super().__init__(x, y)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

class Inky(Entity):
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/ms_pacman', 'Inky.png')), (E_SIZE, E_SIZE))
        super().__init__(x, y)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

class Sue(Entity):
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/ms_pacman', 'Sue.png')), (E_SIZE, E_SIZE))
        super().__init__(x, y)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))