import os

import pygame
from constants import *
from pacman_entity import Entity

WIDTH, HEIGHT = 1400, 1000
P_SIZE = 45



class Player(Entity):
    def __init__(self, x, y):
        self.images = []
        for image in range(1,5):
            self.images.append(pygame.transform.scale(
                pygame.image.load(os.path.join('assets/ms_pacman', f'Ms.pac-man{image}.png')), (P_SIZE, P_SIZE)))

        self.mask = pygame.mask.from_surface(self.images[0])
        super().__init__(x, y)

    def draw(self, win):
        win.blit(self.images[0], (self.x, self.y))
