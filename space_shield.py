import pygame

GREEN = (0, 255, 15)

# shield
S_SIZE = 10
S_SHAPE = [
    '  xxxxxxx',
    ' xxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxx     xxx',
    'xx       xx']


class Shield:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mask = pygame.mask.Mask((S_SIZE, S_SIZE), True)

    def draw(self, win):
        pygame.draw.rect(win, GREEN, (self.x, self.y, S_SIZE, S_SIZE))