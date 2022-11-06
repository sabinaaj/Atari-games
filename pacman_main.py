from pacman_player import *
from pacman_ghosts import *


class Game:
    def __init__(self):
        self.map = Map()
        self.map.get_map()

        self.player = Player(13 * TILE_SIZE + E_SIZE // 2, 22 * TILE_SIZE + 45)
        self.counter = 0

        self.blinky = Blinky(11 * TILE_SIZE + 2, 14 * TILE_SIZE + 10)
        self.pinky = Pinky(12 * TILE_SIZE + 15, 14 * TILE_SIZE + 10)
        self.inky = Inky(14 * TILE_SIZE, 14 * TILE_SIZE + 10)
        self.sue = Sue(15 * TILE_SIZE + 15, 14 * TILE_SIZE + 10)

    def draw(self, win):
        win.fill(DARK_GRAY)

        self.map.draw(win)
        self.player.draw(win, self.counter // 5)

        self.blinky.draw(win)
        self.pinky.draw(win)
        self.inky.draw(win)
        self.sue.draw(win)

        if self.counter >= 19:
            self.counter = 0
        else:
            self.counter += 1

        pygame.display.update()

    def player_movement(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.change_direction(LEFT)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.change_direction(RIGHT)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.change_direction(UP)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.change_direction(DOWN)


def gameloop():
    run = True
    game = Game()
    win = pygame.display.set_mode((game.map.columns * TILE_SIZE, HEIGHT), pygame.RESIZABLE)

    while run:
        pygame.time.Clock().tick(FPS)

        keys = pygame.key.get_pressed()
        game.player_movement(keys)
        game.player.check_position(game.map.map_list)
        game.player.eat_circle()
        game.player.move()

        game.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
