import os

import pygame

WIDTH, HEIGHT = 1400, 1000

# invaders
I_SIZE = 75
I_SPEED = 10

# mystery ship
M_SIZE = 125
M_SPEED = 4

INVADER1a = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'invader1a.png')), (I_SIZE, I_SIZE))
INVADER2a = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'invader2a.png')), (I_SIZE, I_SIZE))
INVADER3a = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'invader3a.png')), (I_SIZE, I_SIZE))
INVADER1b = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'invader1b.png')), (I_SIZE, I_SIZE))
INVADER2b = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'invader2b.png')), (I_SIZE, I_SIZE))
INVADER3b = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'invader3b.png')), (I_SIZE, I_SIZE))
MYSTERY_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'mystery_ship.ico')), (M_SIZE, M_SIZE))


class Invader:
    INVADERS = [
        (INVADER1a, INVADER1b, 30),
        (INVADER2a, INVADER2b, 20),
        (INVADER3a, INVADER3b, 10),
    ]

    def __init__(self, x, y, typ):
        self.x = x
        self.y = y
        self.is_live = True
        self.image1, self.image2, self.points = self.INVADERS[typ - 1]
        self.change_image = False
        self.mask = pygame.mask.from_surface(self.image1)

    def draw(self, win):

        if self.change_image:
            win.blit(self.image1, (self.x, self.y))
        else:
            win.blit(self.image2, (self.x, self.y))

    def move(self, direction):
        self.change_image = not self.change_image
        if direction == -1:
            self.x -= I_SPEED
        elif direction == 0:
            self.y += I_SPEED
        elif direction == 1:
            self.x += I_SPEED


class MysteryShip:
    def __init__(self, direction):
        # -1 = left, 1 = right
        self.direction = direction
        self.x = WIDTH + I_SIZE if direction == -1 else 0 - I_SIZE
        self.y = 75
        self.points = 200
        self.image = MYSTERY_SHIP
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        if self.direction == -1:
            self.x -= M_SPEED
        else:
            self.x += M_SPEED
