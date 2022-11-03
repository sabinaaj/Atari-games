import random
from time import sleep

import pygame

import main
from constants import *
from space_invader import I_SIZE, MysteryShip, Invader
from space_laser import Laser
from space_player import Player, P_WIDTH
from space_shield import S_SIZE, S_SHAPE, Shield

ROWS, COLUMNS = 5, 11

X_MARGIN = (WIDTH - 11 * (I_SIZE + 10)) // 2
SPACE_BETWEEN = (WIDTH - 2 * X_MARGIN - 44 * S_SIZE) // 3


class Game:
    def __init__(self):
        self.player = Player(WIDTH // 2 - P_WIDTH // 2)
        self.player_laser = None

        self.invaders = self.invaders_setup()
        self.invaders_dir = RIGHT
        self.invaders_lasers = []
        self.row_counter = 0
        self.down = False

        self.mystery_ship = None
        self.mystery_ship_spawn_time = random.randint(500, 1000)

        self.shields = self.shield_setup()
        self.score = 0

    def draw(self, win):
        win.fill(DARK_GRAY)

        main.draw_text(win, f'SCORE: {self.score}', 150, 40, 40)
        main.draw_text(win, f'LIVES: {self.player.lives}', WIDTH - 150, 40, 40)

        for invader_laser in self.invaders_lasers:
            invader_laser.move()
            invader_laser.draw(win)

        for invader in self.invaders:
            invader.draw(win)

        for shield in self.shields:
            shield.draw(win)

        if self.player_laser is not None:
            self.player_laser.draw(win)

        if self.mystery_ship is not None:
            self.mystery_ship.draw(win)

        self.player.draw(win)

        pygame.display.update()

    # Handles player movement and shooting based on pressed keys
    def player_movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(LEFT)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(RIGHT)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.player_laser is None:
                self.player_laser = self.player.shoot_laser()

    def player_shoot(self):
        if self.player_laser is not None:
            self.player_laser.move()
            if self.player_laser.y < 0:
                self.player_laser = None

    def player_laser_collision(self):
        hit = False
        if self.player_laser is not None:
            for shield in self.shields:
                if collide(self.player_laser, shield):
                    self.shields.remove(shield)
                    hit = True
                    break
            for invader in self.invaders:
                if collide(self.player_laser, invader):
                    self.score += invader.points
                    self.invaders.remove(invader)
                    hit = True
                    break
            if self.mystery_ship is not None:
                if collide(self.player_laser, self.mystery_ship):
                    self.score += self.mystery_ship.points
                    self.mystery_ship = None
                    hit = True

            if hit:
                self.player_laser = None

    # Draws invaders on display in rectangle
    def invaders_setup(self):
        invaders = []
        for row_idx, row in enumerate(range(ROWS)):
            for col_idx, col in enumerate(range(COLUMNS)):
                # calculate x of every invader, so they are in the middle
                x = X_MARGIN + col_idx * (I_SIZE + 10)
                y = 200 + row_idx * (I_SIZE + 5)

                if row == 0:
                    invader = Invader(x, y, 1)
                elif row == 1 or row == 2:
                    invader = Invader(x, y, 2)
                else:
                    invader = Invader(x, y, 3)

                invaders.append(invader)
        return invaders

    def invader_laser_collision(self):
        for laser in self.invaders_lasers:
            for shield in self.shields:
                if collide(laser, shield):
                    self.shields.remove(shield)
                    self.invaders_lasers.remove(laser)
                    break

            if collide(laser, self.player):
                self.player.lives -= 1
                if self.player.lives > 0:
                    self.player.x = WIDTH // 2 - P_WIDTH // 2
                    sleep(1)
                    self.invaders_lasers.remove(laser)
                    break

    def invaders_movement(self):
        for invader in self.invaders:
            if invader.x >= WIDTH - I_SIZE:
                self.invaders_go_down()
                self.invaders_dir = LEFT
            elif invader.x <= 0:
                self.invaders_go_down()
                self.invaders_dir = RIGHT
            invader.move(self.invaders_dir)

    def invaders_go_down(self):
        self.row_counter += 1
        for invader in self.invaders:
            invader.move(DOWN)

    def invader_shoot(self):
        invader = random.choice(self.invaders)
        laser = Laser(invader.x + I_SIZE // 2, invader.y, False)
        self.invaders_lasers.append(laser)

    def mystery_ship_handler(self):
        self.mystery_ship_spawn_time -= 1
        if self.mystery_ship_spawn_time <= 0:
            self.mystery_ship = MysteryShip(random.choice([-1, 1]))
            self.mystery_ship_spawn_time = random.randint(500, 1000)

        if self.mystery_ship is not None:
            self.mystery_ship.move()
            if self.mystery_ship.direction == -1 and self.mystery_ship.x + I_SIZE < 0:
                self.mystery_ship = None
            elif self.mystery_ship.direction == 1 and self.mystery_ship.x > WIDTH:
                self.mystery_ship = None

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


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def gameloop(win):
    run = True

    game = Game()

    invader_shoot = pygame.USEREVENT
    pygame.time.set_timer(invader_shoot, 750)

    invader_move = pygame.USEREVENT + 1
    pygame.time.set_timer(invader_move, 300)

    while run:
        pygame.time.Clock().tick(FPS)

        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.player_shoot()
        game.player_laser_collision()

        game.invader_laser_collision()
        game.mystery_ship_handler()

        game.draw(win)

        for event in pygame.event.get():
            if event.type == invader_move:
                game.invaders_movement()
            if event.type == invader_shoot:
                game.invader_shoot()
            if event.type == pygame.QUIT:
                run = False

        # if game.row_counter > 15 or game.player.lives == 0:
        #     main.end_screen('GAME OVER')
        #     run = False
        if len(game.invaders) == 0:
            main.end_screen('YOU WON')
            run = False
