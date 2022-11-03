import os

import pygame

from space_laser import Laser

WIDTH, HEIGHT = 1400, 1000
P_WIDTH, P_HEIGHT = 100, 60
P_SPEED = 5

PLAYER_ICON = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'cannon.png')), (P_WIDTH, P_HEIGHT))


class Player:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT - P_HEIGHT - 20
        self.lives = 3
        self.image = PLAYER_ICON
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self, left):
        # player go left
        if left and self.x >= 0:
            self.x -= P_SPEED
        # player go right
        elif not left and self.x + P_WIDTH <= WIDTH:
            self.x += P_SPEED

    def shoot_laser(self):
        return Laser(self.x + P_WIDTH // 2, self.y, True)
