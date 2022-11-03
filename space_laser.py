import pygame

WHITE = (255, 255, 255)

# laser
L_WIDTH, L_HEIGHT = 5, 15
L_SPEED = 20

class Laser:
    def __init__(self, x, y, up):
        self.x = x
        self.y = y
        # if it's player's laser go up is true and if it's invader's laser go down
        self.up = up
        self.mask = pygame.mask.Mask((L_WIDTH, L_HEIGHT), True)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, L_WIDTH, L_HEIGHT))

    def move(self):
        if self.up:
            self.y -= L_SPEED
        elif not self.up:
            self.y += L_SPEED