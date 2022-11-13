from time import sleep

import main
from pacman_ghosts import *
from pacman_player import *


class Game:
    def __init__(self):
        self.counter = 0

        # map
        self.map = Map()
        self.map.get_map()

        # player
        self.player = Player(13 * TILE_SIZE + E_SIZE // 2, 22 * TILE_SIZE + 45)
        self.player.check_position(self.map.map_list)

        # ghosts
        self.blinky = Blinky(11 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Blinky')
        self.pinky = Pinky(12 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Pinky')
        self.inky = Inky(14 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Inky')
        self.sue = Sue(15 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2, 'Sue')
        self.ghosts = [self.blinky, self.pinky, self.inky, self.sue]
        for ghost in self.ghosts:
            ghost.check_position(self.map.map_list)
            ghost.change_direction()
            ghost.get_next_tile(self.map.map_list)

        # 0 = False, 1 = True, 2 = frightened mode ends
        self.frightened = 0
        self.chase = False

    # Updates screen every frame
    def draw(self, win):
        win.fill(DARK_GRAY)

        win.blit(BACK, (25, 10))

        main.draw_text(win, f'SCORE: {self.player.score}', x=200, y=25, size=35)
        main.draw_text(win, f'LIVES: {self.player.lives}', x=PACMAN_WIN_WIDTH - 150, y=25, size=35)

        self.map.draw(win)
        self.player.draw(win, self.counter // 5)

        for ghost in self.ghosts:
            ghost.draw(win, self.frightened, self.counter // 10)

        # counter for image changes
        if self.counter >= 19:
            self.counter = 0
        else:
            self.counter += 1

        pygame.display.update()

    # Handles player movement based on keys
    def player_movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.change_direction(LEFT)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.change_direction(RIGHT)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.change_direction(UP)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.change_direction(DOWN)

    def player_handler(self, frightened_mode):
        self.player.check_position(self.map.map_list)

        if self.player.eat_pellet():
            self.map.pellets -= 1

        if self.player.eat_power_pellet():
            self.map.pellets -= 1
            self.frightened = 1
            pygame.time.set_timer(frightened_mode, 4000)

            for ghost in self.ghosts:
                ghost.turn_around(self.map.map_list)

        self.player.go_through_tunnel()
        self.player.move()

    # Handles ghosts based on their state
    def ghost_handler(self):
        for ghost in self.ghosts:
            if not ghost.eaten:
                if ghost.in_box:
                    if ghost.tile == self.map.map_list[10][13]:
                        ghost.in_box = False
                else:
                    if self.chase:
                        if ghost != self.inky:
                            ghost.chase(self.player.x, self.player.y, self.player.direction)
                        else:
                            ghost.chase(self.player.x, self.player.y, self.player.direction, self.blinky.x,
                                        self.blinky.y)
                    else:
                        ghost.scatter()
            else:
                ghost.get_in_box(self.map.map_list)

            ghost.go_through_tunnel()
            ghost.move(self.map.map_list, self.frightened)

    # Handles collision between player and ghosts
    def player_ghost_collision(self):
        for ghost in self.ghosts:
            # if ghost and player collide
            if self.player.x < ghost.x + E_SIZE and \
                    self.player.x + E_SIZE > ghost.x and \
                    self.player.y < ghost.y + E_SIZE and \
                    self.player.y + E_SIZE > ghost.y:

                if self.frightened:
                    ghost.eaten = True
                    self.player.score += 400
                else:
                    if not ghost.eaten:
                        self.player.lives -= 1
                        sleep(1)
                        self.reset()

    def reset(self):
        self.player.x, self.player.y = 13 * TILE_SIZE + E_SIZE // 2, 22 * TILE_SIZE + 45
        self.player.direction = None
        self.player.check_position(self.map.map_list)

        self.blinky.x, self.blinky.y = 11 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2
        self.pinky.x, self.pinky.y = 12 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2
        self.inky.x, self.inky.y = 14 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2
        self.sue.x, self.sue.y = 15 * TILE_SIZE + TILE_SIZE // 2, 14 * TILE_SIZE + TILE_SIZE // 2
        for ghost in self.ghosts:
            ghost.in_box = True
            ghost.target = (13 * TILE_SIZE, 12 * TILE_SIZE)
            ghost.check_position(self.map.map_list)
            ghost.change_direction()
            ghost.get_next_tile(self.map.map_list)


def gameloop():
    run = True
    win = pygame.display.set_mode((PACMAN_WIN_WIDTH, HEIGHT), pygame.RESIZABLE)

    game = Game()

    change_chase = pygame.USEREVENT
    pygame.time.set_timer(change_chase, 20000 if game.chase else 7000)

    frightened_mode = pygame.USEREVENT + 1
    end_of_frightened_mode = pygame.USEREVENT + 2

    while run:
        pygame.time.Clock().tick(FPS)

        # back arrow
        mouse_pos = pygame.mouse.get_pos()
        back_rec = pygame.Rect(25, 10, BACK_WIDTH, BACK_HEIGHT)

        # player
        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.player_handler(frightened_mode)

        # ghosts
        game.ghost_handler()
        game.player_ghost_collision()

        game.draw(win)

        for event in pygame.event.get():
            if event.type == change_chase:
                game.chase = not game.chase
                pygame.time.set_timer(change_chase, 20000 if game.chase else 5000)

            if event.type == frightened_mode:
                if game.frightened == 1:
                    pygame.time.set_timer(frightened_mode, 0)
                    pygame.time.set_timer(end_of_frightened_mode, 1000)
                    game.frightened = 2

            if event.type == end_of_frightened_mode:
                if game.frightened == 2:
                    pygame.time.set_timer(end_of_frightened_mode, 0)
                    game.frightened = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rec.collidepoint(mouse_pos):
                    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                    run = False
                    main.main()

            if event.type == pygame.QUIT:
                run = False

        # checks end of game
        if game.player.lives == 0:
            win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            main.end_screen('GAME OVER', f'SCORE: {game.player.score}')
            run = False
        if game.map.pellets == 0:
            win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            main.end_screen('YOU WON', f'SCORE: {game.player.score}')
            run = False
