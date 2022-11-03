
import pygame
from constants import *

E_SPEED = 5

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None

    def move(self, direction):
        if direction == LEFT:
            self.x -= E_SPEED
        elif direction == DOWN:
            self.y += E_SPEED
        elif direction == RIGHT:
            self.x += E_SPEED
        elif direction == UP:
            self.y -= E_SPEED
