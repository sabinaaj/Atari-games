import os
import random
import pygame

import main

WIDTH, HEIGHT = 1400, 1000
FPS = 60
WHITE = (255, 255, 255)
DARK_GRAY = (18, 18, 18)
GREEN = (0, 255, 15)

P_WIDTH, P_HEIGHT = 100, 60
P_SPEED = 5

I_WIDTH = I_HEIGHT = 75
I_SPEED = 3
ROWS, COLUMNS = 5, 11

S_SIZE = 10
S_SHAPE = [
    '  xxxxxxx',
    ' xxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxx     xxx',
    'xx       xx']

L_WIDTH, L_HEIGHT = 5, 15
L_SPEED = 12

X_MARGIN = (WIDTH - 11 * (I_WIDTH + 10)) // 2
SPACE_BETWEEN = (WIDTH - 2 * X_MARGIN - 44 * S_SIZE) // 3

PLAYER_ICON = pygame.transform.scale(
    pygame.image.load(os.path.join("assets/space_invaders", "cannon.png")), (P_WIDTH, P_HEIGHT))
INVADER1 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets/space_invaders", "invader1.ico")), (I_WIDTH, I_HEIGHT))
INVADER2 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets/space_invaders", "invader2.ico")), (I_WIDTH, I_HEIGHT))
INVADER3 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets/space_invaders", "invader3.ico")), (I_WIDTH, I_HEIGHT))


class Player:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT - P_HEIGHT - 20
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

    def shoot_laser(self):
        return Laser(self.x + P_WIDTH // 2, self.y, True)


class Invader:
    def __init__(self, x, y, image, points):
        self.x = x
        self.y = y
        self.is_live = True
        self.image = image
        self.points = points

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == -1:
            self.x -= I_SPEED
        elif direction == 0:
            self.y += I_SPEED
        elif direction == 1:
            self.x += I_SPEED


class Shield:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, GREEN, (self.x, self.y, S_SIZE, S_SIZE))


class Laser:
    def __init__(self, x, y, up):
        self.x = x
        self.y = y
        # if it's player's laser go up is true and if it's invader's laser go down
        self.up = up

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, L_WIDTH, L_HEIGHT))

    def move(self):
        if self.up:
            self.y -= L_SPEED
        elif not self.up:
            self.y += L_SPEED


class Game:
    def __init__(self):
        self.player = Player(WIDTH // 2 - P_WIDTH // 2)
        self.player_laser = None

        self.invaders = self.invaders_setup(ROWS, COLUMNS)
        # direction, -1 = left, 0 = down, 1 = right
        self.invaders_dir = 1
        self.invaders_lasers = []

        self.shields = self.shield_setup()
        self.score = 0

    def draw(self, win):
        win.fill(DARK_GRAY)

        main.draw_text(win, f'SCORE: {self.score}', 150, 40, 40)
        main.draw_text(win, f'LIVES: {self.player.lives}', WIDTH - 150, 40, 40)

        for invader in self.invaders:
            invader.move(self.invaders_dir)
            invader.draw(win)

        for invader_laser in self.invaders_lasers:
            invader_laser.move()
            invader_laser.draw(win)

        for shield in self.shields:
            shield.draw(win)

        if self.player_laser is not None:
            self.player_laser.draw(win)

        self.player.draw(win)

        pygame.display.update()

    # Handles player movement and shooting based on pressed keys
    def player_movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(True)
        if keys[pygame.K_RIGHT]  or keys[pygame.K_d]:
            self.player.move(False)
        if keys[pygame.K_UP]  or keys[pygame.K_w]:
            if self.player_laser is None:
                self.player_laser = self.player.shoot_laser()

    def player_shoot(self):
        if self.player_laser is not None:
            self.player_laser.move()
            if self.player_laser.y < 0:
                self.player_laser = None

    # Draws invaders on display in rectangle
    def invaders_setup(self, rows, cols):
        invaders = []
        for row_idx, row in enumerate(range(rows)):
            for col_idx, col in enumerate(range(cols)):
                # calculate x of every invader, so they are in the middle
                x = X_MARGIN + col_idx * (I_WIDTH + 10)
                y = 100 + row_idx * (I_HEIGHT + 5)

                if row == 0:
                    invader = Invader(x, y, INVADER3, 30)
                elif row == 1 or row == 2:
                    invader = Invader(x, y, INVADER2, 20)
                else:
                    invader = Invader(x, y, INVADER1, 10)

                invaders.append(invader)
        return invaders

    def invaders_movement(self):

        for invader in self.invaders:
            if invader.x >= WIDTH - I_WIDTH:
                self.invaders_go_down()
                self.invaders_dir = -1
            elif invader.x <= 0:
                self.invaders_go_down()
                self.invaders_dir = 1

    def invaders_go_down(self):
        for invader in self.invaders:
            invader.move(0)

    def invader_shoot(self):
        invader = random.choice(self.invaders)
        laser = Laser(invader.x - I_WIDTH//2, invader.y, False)
        self.invaders_lasers.append(laser)


    def shield_setup(self):
        shields = []
        y = HEIGHT - 250
        for shield in range(4):
            x = X_MARGIN + (11 * S_SIZE + SPACE_BETWEEN) * shield

            for row_idx, row in enumerate(S_SHAPE):
                for col_idx, col in enumerate(row):
                    if col == 'x':
                        shield_piece = Shield(x + S_SIZE * col_idx, y + row_idx * S_SIZE)
                        shields.append(shield_piece)
        return shields


def gameloop(win):
    run = True

    game = Game()

    invader_shoot = pygame.USEREVENT
    pygame.time.set_timer(invader_shoot, 1000)


    while run:
        pygame.time.Clock().tick(FPS)

        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.player_shoot()

        game.invaders_movement()

        game.draw(win)

        for event in pygame.event.get():
            if event.type == invader_shoot:
                game.invader_shoot()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
