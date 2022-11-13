import random
from time import sleep

import main
from space_invader import *
from space_player import *
from space_shield import *

ROWS, COLUMNS = 5, 11

# margin between edge of the screen and invaders
X_MARGIN = (WIDTH - 11 * (I_SIZE + 10)) // 2
# space between two shields
SPACE_BETWEEN = (WIDTH - 2 * X_MARGIN - 44 * S_SIZE) // 3


class Game:
    def __init__(self):
        # player
        self.player = Player(WIDTH // 2 - P_WIDTH // 2)
        self.player_laser = None
        self.score = 0

        # invaders
        self.invaders = self.invaders_setup()
        self.invaders_dir = RIGHT
        self.invaders_lasers = []
        self.row_counter = 0
        self.down = False

        # mystery ship
        self.mystery_ship = None
        self.mystery_ship_spawn_time = random.randint(500, 1000)

        # shields
        self.shields = self.shield_setup()

    # Updates screen every frame
    def draw(self, win):
        win.fill(DARK_GRAY)

        win.blit(BACK, (25, 27))

        main.draw_text(win, f'SCORE: {self.score}', x=200, y=40, size=40)
        main.draw_text(win, f'LIVES: {self.player.lives}', x=WIDTH - 150, y=40, size=40)

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

    # Handles player laser movement
    def player_shoot(self):
        if self.player_laser is not None:
            self.player_laser.move()
            if self.player_laser.y < 0:
                self.player_laser = None

    # Checks collision between player laser and shields, invaders and mystery ship
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
        for row in range(ROWS):
            for col in range(COLUMNS):
                # calculate x of every invader, so they are in the middle
                x = X_MARGIN + col * (I_SIZE + 10)
                y = 200 + row * (I_SIZE + 5)

                if row == 0:
                    invader = Invader(x, y, col, 1)
                elif row == 1 or row == 2:
                    invader = Invader(x, y, col, 2)
                else:
                    invader = Invader(x, y, col, 3)

                invaders.append(invader)

        return invaders

    # Checks collision between invader's lasers and shields and player
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

    # Changes invaders direction based on their position
    def invaders_movement(self):
        down = False

        for invader in self.invaders:
            if invader.x >= WIDTH - (I_SIZE + 10) * (11 - invader.column):
                down = True
                invader.move(DOWN)
                self.invaders_dir = LEFT
            elif invader.x <= 0 + (I_SIZE + 10) * invader.column:
                down = True
                invader.move(DOWN)
                self.invaders_dir = RIGHT

            invader.move(self.invaders_dir)

        if down:
            self.row_counter += 1

    # Makes player laser
    def invader_shoot(self):
        invader = random.choice(self.invaders)
        laser = Laser(invader.x + I_SIZE // 2, invader.y, False)
        self.invaders_lasers.append(laser)

    # Handles mystery ship
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

    # Calculate shield position and initialize it
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


# Checks if mask of two object collides
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

        # back arrow
        mouse_pos = pygame.mouse.get_pos()
        back_rec = pygame.Rect(25, 27, BACK_WIDTH, BACK_HEIGHT)

        # player
        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.player_shoot()
        game.player_laser_collision()

        # invaders
        game.invader_laser_collision()
        game.mystery_ship_handler()

        game.draw(win)

        for event in pygame.event.get():
            if event.type == invader_move:
                game.invaders_movement()
            if event.type == invader_shoot:
                game.invader_shoot()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rec.collidepoint(mouse_pos):
                    run = False
                    main.main()
            if event.type == pygame.QUIT:
                run = False

        # checks end of game
        if game.row_counter > 15 or game.player.lives == 0:
            main.end_screen('GAME OVER', f'SCORE: {game.score}')
            run = False
        if len(game.invaders) == 0:
            main.end_screen('YOU WON', f'SCORE: {game.score}')
            run = False
