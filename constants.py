import os
import pygame

# win
WIDTH, HEIGHT = 1400, 1000
PACMAN_WIN_WIDTH = 840
FPS = 60

# colors
WHITE = (255, 255, 255)
DARK_GRAY = (18, 18, 18)

# directions
LEFT = -1
DOWN = 0
RIGHT = 1
UP = 2

# back arrow
BACK_WIDTH, BACK_HEIGHT = 40, 30
BACK = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'back.png')), (BACK_WIDTH, BACK_HEIGHT))