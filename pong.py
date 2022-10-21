from random import choice

import pygame

import main

WIDTH, HEIGHT = 1400, 1000
P_WIDTH, P_HEIGHT = 40, 250
P_SPEED = 5
B_RADIUS = 14
B_SPEED = 8
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
        # paddle go up
        if up and self.y >= 0:
            self.y -= P_SPEED
        # paddle go down
        elif not up and self.y + P_HEIGHT <= HEIGHT:
            self.y += P_SPEED

    def ai_move(self, ball):
        y_middle = self.y + P_HEIGHT // 2

        # ball is under the paddle
        if ball.y > self.y + P_HEIGHT:
            self.move(False)
        # ball is above the paddle
        elif ball.y < self.y:
            self.move(True)
        # ball is in 2/4 of the paddle
        elif self.y + P_HEIGHT//4 * 2 < ball.y <= y_middle:
            self.move(True)
        # ball is in 3/4 of the paddle
        elif P_HEIGHT + P_HEIGHT//4 * 3 < ball.y < y_middle:
            self.move(False)

    # Handle ball and paddle collision
    def ball_collision(self, ball):
        ball.x_speed *= -1
        y_middle = self.y + P_HEIGHT // 2
        difference_in_y = y_middle - ball.y
        y_speed = difference_in_y // ((P_HEIGHT // 2) // B_SPEED)
        ball.y_speed = -1 * y_speed


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

    # Draws divider in the middle
    for idx in range(40):
        if idx % 2 == 1:
            pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, HEIGHT // 40 * idx - HEIGHT // 80, 10, HEIGHT // 40))

    pygame.display.update()


# Checks what keys are pressed and move paddles
def paddle_movement(keys, r_paddle, l_paddle, multiplayer):
    if keys[pygame.K_w]:
        l_paddle.move(True)
    if keys[pygame.K_s]:
        l_paddle.move(False)
    if keys[pygame.K_UP] and multiplayer:
        r_paddle.move(True)
    if keys[pygame.K_DOWN] and multiplayer:
        r_paddle.move(False)


def ball_movement(ball, r_paddle, l_paddle):
    if ball.y - B_RADIUS <= 0 or ball.y + 5 + B_RADIUS >= HEIGHT:
        ball.y_speed *= -1

    if ball.x_speed < 0:
        if l_paddle.y <= ball.y <= l_paddle.y + P_HEIGHT:  # if paddle touches the ball
            if ball.x - B_RADIUS <= l_paddle.x + P_WIDTH:
                l_paddle.ball_collision(ball)
    else:
        if r_paddle.y <= ball.y <= r_paddle.y + P_HEIGHT:
            if ball.x + B_RADIUS >= r_paddle.x:
                r_paddle.ball_collision(ball)

    ball.move()


# Changes coordinates and ball speed to default values
def reset(ball, r_paddle, l_paddle):
    l_paddle.x, l_paddle.y = 40, HEIGHT // 2 - P_HEIGHT // 2
    r_paddle.x, r_paddle.y = WIDTH - P_WIDTH - 40, HEIGHT // 2 - P_HEIGHT // 2
    ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    ball.x_speed, ball.y_speed = choice([-B_SPEED, B_SPEED]), choice([-B_SPEED, 0, B_SPEED])


# Draws score on display
def draw_score(win, x, score):
    font = pygame.font.Font(None, 150)
    text_on_display = font.render(str(score), True, WHITE)
    text_rect = text_on_display.get_rect()
    text_rect.center = (x, 50)
    win.blit(text_on_display, text_rect)

# Initializes paddles and ball and handle gameloop
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
        paddle_movement(keys, r_paddle, l_paddle, multiplayer)
        ball_movement(ball, r_paddle, l_paddle)
        if not multiplayer:
            r_paddle.ai_move(ball)

        if ball.x <= 0:
            reset(ball, r_paddle, l_paddle)
            r_score += 1
        if ball.x >= WIDTH:
            reset(ball, r_paddle, l_paddle)
            l_score += 1

        if l_score > MAX_SCORE:
            run = False
            if multiplayer:
                main.end_screen('LEFT PLAYER WON')
            else:
                main.end_screen('YOU WON')

        if r_score > MAX_SCORE:
            run = False
            if multiplayer:
                main.end_screen('RIGHT PLAYER WON')
            else:
                main.end_screen('YOU LOST')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()