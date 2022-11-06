import os

import pygame

from constants import *

# invaders
I_SIZE = 75
I_SPEED = 10

# mystery ship
M_SIZE = 125
M_SPEED = 4

INVADER_IMAGES = []
for image in range(1, 4):
    INVADER_IMAGES.append(pygame.transform.scale(
        pygame.image.load(os.path.join('assets/space_invaders', f'invader{image}a.png')), (I_SIZE, I_SIZE)))
    INVADER_IMAGES.append(pygame.transform.scale(
        pygame.image.load(os.path.join('assets/space_invaders', f'invader{image}b.png')), (I_SIZE, I_SIZE)))

MYSTERY_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'mystery_ship.ico')), (M_SIZE, M_SIZE))


class Invader:
    INVADER_TYPES = [
        (INVADER_IMAGES[0], INVADER_IMAGES[1], 30),
        (INVADER_IMAGES[2], INVADER_IMAGES[3], 20),
        (INVADER_IMAGES[4], INVADER_IMAGES[5], 10),
    ]

    def __init__(self, x, y, column, typ):
        self.x = x
        self.y = y
        self.column = column
        self.is_live = True
        self.image1, self.image2, self.points = self.INVADER_TYPES[typ - 1]
        self.change_image = False
        self.mask = pygame.mask.from_surface(self.image1)

    def draw(self, win):

        if self.change_image:
            win.blit(self.image1, (self.x, self.y))
        else:
            win.blit(self.image2, (self.x, self.y))

    def move(self, direction):
        self.change_image = not self.change_image
        if direction == LEFT:
            self.x -= I_SPEED
        elif direction == DOWN:
            self.y += I_SPEED
        elif direction == RIGHT:
            self.x += I_SPEED


class MysteryShip:
    def __init__(self, direction):
        self.direction = direction
        self.x = WIDTH + I_SIZE if direction == LEFT else 0 - I_SIZE
        self.y = 75
        self.points = 200
        self.image = MYSTERY_SHIP
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        if self.direction == LEFT:
            self.x -= M_SPEED
        else:
            self.x += M_SPEED
