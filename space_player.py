from constants import *
from space_laser import Laser

# player
P_WIDTH, P_HEIGHT = 100, 60
P_SPEED = 5

PLAYER_ICON = pygame.transform.scale(
    pygame.image.load(os.path.join('assets/space_invaders', 'cannon.png')), (P_WIDTH, P_HEIGHT))


class Player:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT - P_HEIGHT - 20
        self.lives = 3
        self.image = PLAYER_ICON
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    # Change player x coordinate so player go right or left
    def move(self, direction):
        if direction == LEFT and self.x >= 0:
            self.x -= P_SPEED
        elif direction == RIGHT and self.x + P_WIDTH <= WIDTH:
            self.x += P_SPEED

    # Makes player laser based on player coordinates
    def shoot_laser(self):
        return Laser(self.x + P_WIDTH // 2, self.y, True)
