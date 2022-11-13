from constants import *

# laser
L_WIDTH, L_HEIGHT = 5, 15
L_SPEED = 20


class Laser:
    def __init__(self, x, y, up):
        self.x = x
        self.y = y
        # player laser go up and invader laser go down
        self.up = up
        self.mask = pygame.mask.Mask((L_WIDTH, L_HEIGHT), True)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, L_WIDTH, L_HEIGHT))

    def move(self):
        if self.up:
            self.y -= L_SPEED
        elif not self.up:
            self.y += L_SPEED
