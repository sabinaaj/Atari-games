from random import choice

import pygame

WIDTH, HEIGHT = 1400, 1000
P_WIDTH, P_HEIGHT = 40, 250
P_SPEED = 5
B_RADIUS = 14
B_SPEED = 9
MAX_SCORE = 10
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
            self.y -= P_SPEED
        else:
            self.y += P_SPEED


class Ball:
    def __init__(self, x, y, x_speed, y_speed):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), B_RADIUS)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed


def draw(win, r_paddle, l_paddle, ball, r_score, l_score):
    win.fill(BLACK)
    r_paddle.draw(win)
    l_paddle.draw(win)
    ball.draw(win)
    draw_score(win, WIDTH // 2 - 50, l_score)
    draw_score(win, WIDTH // 2 + 50, r_score)

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


def ball_movement(ball, r_paddle, l_paddle):
    if ball.y - B_RADIUS <= 0 or ball.y + 5 +B_RADIUS >= HEIGHT:
        ball.y_speed *= -1

    if ball.x_speed < 0:
        if l_paddle.y <= ball.y <= l_paddle.y + P_HEIGHT:  # if paddle touches the ball
            if ball.x - B_RADIUS <= l_paddle.x + P_WIDTH:
                ball_paddle_collision(ball, l_paddle)
    else:
        if r_paddle.y <= ball.y <= r_paddle.y + P_HEIGHT:
            if ball.x + B_RADIUS >= r_paddle.x:
                ball_paddle_collision(ball, r_paddle)

    ball.move()


def ball_paddle_collision(ball, paddle):
    ball.x_speed *= -1
    y_middle = paddle.y + P_HEIGHT // 2
    difference_in_y = y_middle - ball.y
    y_speed = difference_in_y // ((P_HEIGHT // 2) // B_SPEED)
    ball.y_speed = -1 * y_speed


def reset(ball, r_paddle, l_paddle):
    l_paddle.x, l_paddle.y = 40, HEIGHT // 2 - P_HEIGHT // 2
    r_paddle.x, r_paddle.y = WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2
    ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    ball.x_speed, ball.y_speed = choice([-B_SPEED, B_SPEED]), choice([-B_SPEED, 0, B_SPEED])

def draw_score(win, x, score):
    font = pygame.font.Font(None, 150)
    text_on_display = font.render(str(score), True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (x, 50)
    win.blit(text_on_display, text_rect)

def gameloop(win, multiplayer):
    run = True
    l_paddle = Paddle(40, HEIGHT // 2 - P_HEIGHT // 2)
    r_paddle = Paddle(WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2, choice([-B_SPEED, B_SPEED]), choice([-B_SPEED, 0, B_SPEED]))
    l_score, r_score = 0, 0

    while run:
        pygame.time.Clock().tick(FPS)
        draw(win, r_paddle, l_paddle, ball, r_score, l_score)

        keys = pygame.key.get_pressed()
        paddle_movement(keys, r_paddle, l_paddle)
        ball_movement(ball, r_paddle, l_paddle)

        if ball.x <= 0:
            reset(ball, r_paddle, l_paddle)
            l_score += 1
        if ball.x >= WIDTH:
            reset(ball, r_paddle, l_paddle)
            r_score += 1

        if l_score > MAX_SCORE:
            run = False
        if r_score > MAX_SCORE:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
