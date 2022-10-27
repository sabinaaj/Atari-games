import os

import pygame

import main

WIDTH, HEIGHT = 1400, 1000
FPS = 60
WHITE = (255, 255, 255)
DARK_GRAY = (18, 18, 18)
P_WIDTH, P_HEIGHT = 80, 40
P_SPEED = 5
I_WIDTH = I_HEIGHT = 75
ROWS, COLUMNS = 5, 11

PLAYER_ICON = pygame.transform.scale(pygame.image.load(os.path.join("assets/space_invaders", "cannon.png")), (P_WIDTH, P_HEIGHT))
INVADER1 = pygame.transform.scale(pygame.image.load(os.path.join("assets/space_invaders", "invader1.ico")), (I_WIDTH, I_HEIGHT))
INVADER2 = pygame.transform.scale(pygame.image.load(os.path.join("assets/space_invaders", "invader2.ico")), (I_WIDTH, I_HEIGHT))
INVADER3 = pygame.transform.scale(pygame.image.load(os.path.join("assets/space_invaders", "invader3.ico")), (I_WIDTH, I_HEIGHT))


class Player:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT - P_HEIGHT - 20
        self.shots = 1
        self.lives = 3
        self.image = PLAYER_ICON

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self, left):
        # player go left
        if left and self.x >= 0:
            self.x -= P_SPEED
        # player go right
        elif not left and self.x + P_WIDTH <= WIDTH:
            self.x += P_SPEED


class Invader:
    def __init__(self, x, y, image, points):
        self.x = x
        self.y = y
        self.is_live = True
        self.image = image
        self.points = points

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Shield:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        self.player = Player(WIDTH // 2 - P_WIDTH // 2)
        self.invaders = self.invaders_setup(ROWS, COLUMNS)
        self.score = 0

    def draw(self, win):
        win.fill(DARK_GRAY)

        main.draw_text(win, f'SCORE: {self.score}', 150, 40, 40)
        main.draw_text(win, f'LIVES: {self.player.lives}', WIDTH - 150, 40, 40)

        for invader in self.invaders:
            invader.draw(win)

        self.player.draw(win)

        pygame.display.update()

    # Handles player movement based on pressed keys
    def player_movement(self, keys):
        if keys[pygame.K_LEFT]:
            self.player.move(True)
        if keys[pygame.K_RIGHT]:
            self.player.move(False)

    # Draws invaders on display in regtangle
    def invaders_setup(self, rows, cols):
        invaders = []
        for row_idx, row in enumerate(range(rows)):
            for col_idx, col in enumerate(range(cols)):
                # calculate x of every invader, so they are in the middle
                x = (WIDTH - 11 * (I_WIDTH + 10)) // 2 + col_idx * (I_WIDTH + 10)
                y = 100 + row_idx * (I_HEIGHT + 5)

                if row == 0:
                    invader = Invader(x, y, INVADER3, 30)
                elif row == 1 or row == 2:
                    invader = Invader(x, y, INVADER2, 20)
                else:
                    invader = Invader(x, y, INVADER1, 10)

                invaders.append(invader)
        return invaders


def gameloop(win):
    run = True

    game = Game()

    while run:
        pygame.time.Clock().tick(FPS)

        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
