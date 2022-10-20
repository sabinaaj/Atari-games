import pygame

WIDTH, HEIGHT = 1400, 1000
P_WIDTH, P_HEIGHT = 40, 250
B_RADIUS = 14
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, P_WIDTH, P_HEIGHT))

    def move(self, up):
        if up:
            self.y -= 5
        else:
            self.y += 5


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), B_RADIUS)


def draw(win, r_paddle, l_paddle, ball):
    win.fill(BLACK)
    r_paddle.draw(win)
    l_paddle.draw(win)
    ball.draw(win)

    for idx in range(40):
        if idx % 2 == 1:
            pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, HEIGHT // 40 * idx - HEIGHT // 80, 10, HEIGHT // 40))

    pygame.display.update()


def paddle_movement(keys, r_paddle, l_paddle):
    if keys[pygame.K_w] and l_paddle.y >= 0:
        l_paddle.move(True)
    if keys[pygame.K_s] and l_paddle.y + P_HEIGHT <= HEIGHT:
        l_paddle.move(False)
    if keys[pygame.K_UP] and r_paddle.y >= 0:
        r_paddle.move(True)
    if keys[pygame.K_DOWN] and r_paddle.y + P_HEIGHT <= HEIGHT:
        r_paddle.move(False)


def gameloop(win, multiplayer):
    run = True
    l_paddle = Paddle(40, HEIGHT // 2 - P_HEIGHT // 2)
    r_paddle = Paddle(WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    while run:
        pygame.time.Clock().tick(FPS)
        draw(win, r_paddle, l_paddle, ball)

        keys = pygame.key.get_pressed()
        paddle_movement(keys, r_paddle, l_paddle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
